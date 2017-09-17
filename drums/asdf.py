
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
AudioSegment.converter = '/Users/Marko/Downloads/Lion_Mountain_Lion_Mavericks_Yosemite_El-Captain_15.05.2017/ffmpeg'
play(AudioSegment.from_file('bass.wav', format="wav").overlay(AudioSegment.from_file('hihat.wav', format="wav")))
# sd.play(data, 44100, blocking=True)
# status = sd.get_status()
# if status:
    # logging.warning(str(status))
