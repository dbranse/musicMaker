import time
import numpy as np
import sounddevice as sd
from pydub import AudioSegment

#sampling rate
fs = 44100



def transform_file(flpath):

    def detect_leading_silence(sound, silence_threshold=-40.0, chunk_size=10):
        trim_ms = 0 # ms
        while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
            trim_ms += chunk_size

        return trim_ms

    sound = AudioSegment.from_file(flpath, format="wav")

    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())

    trimmed_sound = sound[start_trim:-end_trim]

    return trimmed_sound.get_array_of_samples()



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
bpm = 100

#l is the number of beats
l = 100

#will loop until the number of beats is done
for i in range(l):
    # wil loop through the beat array at the correct index
    for sound in beatarr[i%len(beatarr)]:
        # we need to play asyncronously
        sd.play(d[sound], fs, blocking = False)
    # wait until the next beat
    time.sleep(bpm/60)