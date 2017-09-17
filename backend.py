from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pyaudio
import wave
from array import array
import time
import os
import simple_drummer as drums
import magicbox as melody
from threading import Thread

app = Flask(__name__)
api = Api(app)

class Click(Resource):
    isClicked = True; #TODO: SHOULD BE FALSE WHEN ADD IN CLICK SENSOR

    def post(self):
        wasClicked = self.isClicked
        # isClicked = False
        return {'isClicked': wasClicked, 'status': 200}

    def get(self):
        print("HERE")
        print(request.args)
api.add_resource(Click, '/click')

class Sounds(Resource):
    bass = None
    snare = None
    hihat = None
    clap = None
    sing = None

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 4

    def post(self, name):
        if (name == 'makeSong'):
            print("asdfasdfasdf\n\n\n\n\n")
            Thread(target = drums.play_drums).start()
            Thread(target = melody.play_melody, args = ('sing.wav',)).start()

        audio = pyaudio.PyAudio()  # instantiate the pyaudio
        
        time.sleep(5)

        # recording prerequisites
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE,
                            input=True,
                            frames_per_buffer=self.CHUNK)
        
        # starting recording
        frames = []
        
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            data_chunk = array('h', data)
            vol = max(data_chunk)
            if (vol >= 500):
                frames.append(data)

        # end of recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
        # writing to file
        FILE_NAME = name + ".wav"
        wavfile = wave.open(FILE_NAME, 'wb')
        wavfile.setnchannels(self.CHANNELS)
        wavfile.setsampwidth(audio.get_sample_size(self.FORMAT))
        wavfile.setframerate(self.RATE)
        wavfile.writeframes(b''.join(frames))  # append frames recorded to file
        wavfile.close()

        if (name == 'bass'):
            bass = wavfile
        if (name == 'snare'):
            snare = wavfile
        if (name == 'hihat'):
            hihat = wavfile
        if (name == 'clap'):
            clap = wavfile
        if (name == 'sing'):
            sing = wavfile
        return {'status': 200}

api.add_resource(Sounds, '/sound/<name>')

if __name__ == "__main__":
    app.run(host= 'localhost', port= 5555, debug = False)

