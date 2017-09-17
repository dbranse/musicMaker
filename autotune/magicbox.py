import time
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
		sd.play(sample, blocking =  True)
