from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)

class Request(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, location='json')
        parser.add_argument('number', type=int, required=True, location='json')
        args = parser.parse_args(strict=True)

        return -1

    def get(self):
        return request.args

api.add_resource(Request, '/requests')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 5555, debug = False)

