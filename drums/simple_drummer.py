import time
import numpy as np
import sounddevice as sd
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
#sampling rate
fs = 44100

# AudioSegment.converter = '/Users/Marko/Downloads/Lion_Mountain_Lion_Mavericks_Yosemite_El-Captain_15.05.2017/ffmpeg'

def transform_file(flpath):

    def detect_leading_silence(sound, silence_threshold=-30.0, chunk_size=10):
        trim_ms = 0 # ms
        while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
            trim_ms += chunk_size

        return trim_ms

    def detect_max_vol(sound, chunk_size=10):
        trim_ms = 0 # ms
        m = -10000
        m_ind = 0
        while trim_ms+chunk_size < len(sound):
            db = sound[trim_ms:trim_ms+chunk_size].dBFS
            if db > m:
                m = db
                m_ind = trim_ms
            trim_ms += chunk_size

        return trim_ms

    sound = AudioSegment.from_file(flpath, format="wav")

    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())

    trimmed_sound = sound[start_trim:-end_trim]

    return trimmed_sound, detect_max_vol(trimmed_sound)



# these will eventually be music files
bass = transform_file('bass.wav')
snare = transform_file('snare.wav')
hihat = transform_file('hihat.wav')
clap = transform_file('clap.wav')

d = {0: bass, 1: snare, 2: hihat, 3: clap}

beatarr = [[0], [1, 2], [3], [1, 2]] #each element contains things that should play on that beat
simplebeats = [[[0,2],[1,2],[0,2],[1,2]], [[0],[2],[3],[2]], [[0,1,2],[2,3],[1,2],[2,3]], [[0,2],[1,3],[1,2],[1,3]], [[0,2],[1,2],[0,2],[1,2]]]
moderatebeats = [[[0,2],[2],[1,2],[2],[0,2],[2],[1,2,3],[2,3]], [[0], [2],[3],[2],[0], [2,1],[3,1],[2,1]], [[0,2], [2],[3,2],[0,2],[2], [2],[3,2],[2]], [[0,2], [2],[2],[1,3,2],[2], [2],[1,3,2],[2]], [[0,2], [0,2],[3,2],[1,2],[2], [0,2],[3,2],[1,2]]]
advancedbeats = [[[0,2],[2],[0,2],[2],[3,2],[2],[0,3],[2],[1,2],[0,2],[0,2],[2],[3,2],[2,1],[0,3,1],[2,1]], [[0,2],[1,2],[3,2],[1,2],[0,2],[1,2],[3,2],[1,2],[0,2],[1,2],[3,2],[1,2],[0,2],[1,2],[1,2],[1,2]], [[0,2],[2],[2],[2],[0],[],[1,2],[0],[2],[3],[3,2],[],[0,2],[2],[1],[2]], [[0,2], [2],[2],[1,3,2],[2], [2],[1,3,2],[2]], [[0,2],[2],[3,2],[0,2],[0,2],[0,2],[2],[3,2],[0,2],[1,2],[3,2],[1,2],[0,2],[1],[1,2],[1,2]]]
bpm = 120

beatarr = moderatebeats[3]
bpm*=2
#l is the number of beats
l = 100

#will loop until the number of beats is done
for i in range(l):
    # wil loop through the beat array at the correct index
    beat_len = 60/float(bpm)*1000
    s = AudioSegment.silent(beat_len)
    smax = None
    
    for sound in beatarr[i%len(beatarr)]:
        # we need to play asyncronously
        s2, s2max = d[sound]
        s = s.overlay(s2, position = beat_len//2 - s2max)

    Thread(target = play, args = (s,)).start()

    # wait until the next beat
    time.sleep(60/float(bpm))