#!/bin/bash

curl http://localhost:5000/

curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6","am":"0"}' "http://localhost:5000/predict_price"
