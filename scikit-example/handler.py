import json
import pickle

# REF: https://www.kaggle.com/prmohanty/python-how-to-save-and-load-ml-models
model_name = 'model_california_housing.pkl'
with open(model_name, 'rb') as file:  
    model = pickle.load(file)

def predict(event, context):

    body = {
        "message": "OK",
    }

    print("event.get('source')", event.get("source"))

    if event.get("source") == "serverless-plugin-warmup":
        body['message'] = 'WarmUP - Keep the Lambda warm!'

    else: 
        params = event['queryStringParameters']

        medInc = float(params['medInc']) / 100000
        houseAge = float(params['houseAge'])
        aveRooms = float(params['aveRooms'])
        aveBedrms = float(params['aveBedrms'])
        population = float(params['population'])
        aveOccup = float(params['aveOccup'])
        latitude = float(params['latitude'])
        longitude = float(params['longitude'])

        inputVector = [medInc, houseAge, aveRooms, aveBedrms, population, aveOccup, latitude, longitude]
        data = [inputVector]
        predictedPrice = model.predict(data)[0] * 100000 # convert to units of 1 USDs
        predictedPrice = round(predictedPrice, 2)
        body['predictedPrice'] = predictedPrice

    print(body['message'])

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": 'application/json',
            "Access-Control-Allow-Origin": "*"
        }
    }

    return response

def do_main():
    event = {
        'queryStringParameters': {
            'medInc': 200000,
            'houseAge': 10,
            'aveRooms': 4,
            'aveBedrms': 1,
            'population': 800,
            'aveOccup': 3,
            'latitude': 37.54,
            'longitude': -121.72
        }
    }

    response = predict(event, None)
    body = json.loads(response['body'])
    print('Price:', body['predictedPrice'])

    with open('event.json', 'w') as event_file:
        event_file.write(json.dumps(event))
    

#do_main()