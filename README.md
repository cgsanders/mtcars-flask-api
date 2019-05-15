# MTCars Flask API

This program implements a simple Flask API that predicts the MPG of cars based on variables found in the MTCars data set. Users will provide information in JSON format and the API will return a prediction. Linear models are generated on demand based on the variables provided in the JSON request. 

To get sever up and running:
1. Download files
2. Change your current directory to the Docker folder in the downloaded files
3. Enter `docker-compose up`in the terminal
4. To check that the server is running enter `curl http://localhost:5000/`, you should get a list of variables that you can use for prediction
5. You can now ask the API to run predictions with json requets. Here is a sample request `curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6","am":"0"}' "http://localhost:5000/predict_price"`
 
 To stop the API:
 1. Type `ctrl-C` in the terminal window. 
 2. Check for open docker instance with `docker container ls`
 3. Stop an instance with `docker container kill <container-name>``
