from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

class Click(Resource):
    isClicked = True; #TODO: SHOULD BE FALSE WHEN ADD IN CLICK SENSOR

    def post(self):
        wasClicked = self.isClicked
        isClicked = False
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

    def post(self, name):
        # TODO: START RECORDING, STORE IN SOUND VARIABLE
        sound = None

        if (name == 'bass'):
            bass = sound
        if (name == 'snare'):
            snare = sound
        if (name == 'hihat'):
            hihat = sound
        if (name == 'clap'):
            clap = sound
        return {'status': 200}

api.add_resource(Sounds, '/sound/<name>')

if __name__ == "__main__":
    app.run(host= 'localhost', port= 5555, debug = False)

