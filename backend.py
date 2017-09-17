from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

class Click(Resource):
    isClicked = False

    def post(self):
        wasClicked = self.isClicked
        isClicked = False
        return {'isClicked': wasClicked, 'status': 200}

    def get(self):
        print("HERE")
        print(request.args)
api.add_resource(Click, '/click')

if __name__ == "__main__":
    app.run(host= 'localhost', port= 5555, debug = False)

