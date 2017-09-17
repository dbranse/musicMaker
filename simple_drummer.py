import time
import numpy as np
import random
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
import pydub.scipy_effects

#sampling rate
fs = 44100

# AudioSegment.converter = '/Users/Marko/Downloads/Lion_Mountain_Lion_Mavericks_Yosemite_El-Captain_15.05.2017/ffmpeg'

def transform_file(flpath, isbass = False, hi = False):

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

    def match_target_amplitude(sound, target_dBFS):
        change_in_dBFS = target_dBFS - sound.dBFS
        return sound.apply_gain(change_in_dBFS)

    sound = AudioSegment.from_file(flpath, format="wav")

    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())

    trimmed_sound = sound[start_trim:-end_trim]

    if isbass:
        #trimmed_sound = trimmed_sound.low_pass_filter(100, order=1)
        trimmed_sound = trimmed_sound.low_pass_filter(500, order=1)
        trimmed_sound = trimmed_sound.low_pass_filter(2000, order=1)
        trimmed_sound = match_target_amplitude(trimmed_sound, -18)
    elif hi:
        trimmed_sound = match_target_amplitude(trimmed_sound, -30)
    else:
        trimmed_sound = match_target_amplitude(trimmed_sound, -18)

    return trimmed_sound, detect_max_vol(trimmed_sound)

def play_drums():
    bass = transform_file('bass.wav', isbass = True)
    snare = transform_file('snare.wav')
    hihat = transform_file('hihat.wav', hi = True)
    clap = transform_file('clap.wav')

    d = {0: bass, 1: snare, 2: hihat, 3: clap}

    simplebeats = [[[0,2],[1,2],[0,2],[1,2]], [[0],[2],[3],[2]], [[0,1,2],[2,3],[1,2],[2,3]], [[0,2],[1,3],[1,2],[1,3]], [[0,2],[1,2],[0,2],[1,2]]]
    moderatebeats = [[[0,2],[2],[1,2],[2],[0,2],[2],[1,2,3],[2,3]], [[0], [2],[3],[2],[0], [2,1],[3,1],[2,1]], [[0,2], [2],[3,2],[0,2],[2], [2],[3,2],[2]], [[0,2], [2],[2],[1,3,2],[2], [2],[1,3,2],[2]], [[0,2], [0,2],[3,2],[1,2],[2], [0,2],[3,2],[1,2]]]
    advancedbeats = [[[0,2],[2],[0,2],[2],[3,2],[2],[0,3],[2],[1,2],[0,2],[0,2],[2],[3,2],[2,1],[0,3,1],[2,1]], [[0,2],[1,2],[3,2],[1,2],[0,2],[1,2],[3,2],[1,2],[0,2],[1,2],[3,2],[1,2],[0,2],[1,2],[1,2],[1,2]], [[0,2],[2],[2],[2],[0],[],[1,2],[0],[2],[3],[3,2],[],[0,2],[2],[1],[2]], [[0,2], [2],[2],[1,3,2],[2], [2],[1,3,2],[2]], [[0,2],[2],[3,2],[0,2],[0,2],[0,2],[2],[3,2],[0,2],[1,2],[3,2],[1,2],[0,2],[1],[1,2],[1,2]]]

    bpm = 80

    r = int(random.random()%3)+2
    beatarr = moderatebeats[r]
    bpm*=2;

    #l is the number of beats
    l = 10000

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