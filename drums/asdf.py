
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
data = np.array(AudioSegment.from_file('bass.wav', format="wav").get_array_of_samples()).astype(np.float32)
sd.play(data, 44100, blocking=True)
status = sd.get_status()
if status:
    logging.warning(str(status))
