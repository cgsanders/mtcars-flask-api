#!/usr/bin/env python3

import os
from flask import Flask, jsonify, request

import json
from prediction import predict


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def flask_app():
    app = Flask(__name__)


    @app.route('/', methods=['GET'])
    def server_is_up():
        message = 'Server is up!\n'
        message += 'Provide any combination of the following variables with values to predict mpg!\n'
        message +="""mpg 	Miles/(US) gallon
cyl 	Number of cylinders
disp 	Displacement (cu.in.)
hp 	Gross horsepower
drat 	Rear axle ratio
wt 	Weight (1000 lbs)
qsec 	1/4 mile time
vs 	Engine (0 = V-shaped, 1 = straight)
am 	Transmission (0 = automatic, 1 = manual)
gear 	Number of forward gears
carb 	Number of carburetors\n"""
        return message

    @app.route('/predict_price', methods=['POST'])
    def start():
        to_predict = request.json

        print(to_predict)
        pred = predict(to_predict)
        return jsonify({"predict mpg":pred})
    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0')


