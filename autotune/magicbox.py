import time
import random
import librosa
import sounddevice as sd

filename = 'baa.wav'

y, sr = librosa.load(filename)

y, _ = librosa.effects.trim(y)

p = librosa.estimate_tuning(y = y, sr = sr, bins_per_octave=1)


y = librosa.effects.pitch_shift(y, sr, -1*p, bins_per_octave=1)


melody = [(0, 1), (0, 1), (0, 1), (None, 1), (2, 1), (3, 0.5), (3, 0.5), (3, 1), (None, 1), (5, 1), (6, 1), (6, 1)]

beat_length = 0.5
sample_len = librosa.get_duration(y, sr)
for i, j in melody:
    if i is None:
        time.sleep(beat_length*j)
    else:
        target_len = beat_length*j
        sample = librosa.effects.time_stretch(y, 1/(sample_len*target_len))
        sample = librosa.effects.pitch_shift(sample, sr = sr, n_steps = i, bins_per_octave = 12)
        sd.play(sample, blocking = True)

def melody_generator(flexvalue):

    newportion = (((int((random.random())*flexvalue))) % (int(math.sqrt(flexvalue))))/int(math.sqrt(flexvalue))
    pitchshift = newportion*12
    scale = [0, 2, 3, 5, 7, 8, 10, 12];
    scalecounter = 0

    while scalecounter<8:
        temp = scale[scalecounter]
        scale[scalecounter] = temp+pitchshift
        scalecounter += 1

    beatcounter =1
    stepcounter = 0
    while beatcounter <= 16:
        length = int(beatcounter/(newportion ^ 3)) % 4
        pitch = int(beatcounter/(newportion ^ beatcounter)) % 8
        melody[stepcounter]=(pitch,length)
        beatcounter += length
        stepcounter += 1
