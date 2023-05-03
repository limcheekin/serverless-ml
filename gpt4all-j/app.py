from gpt4allj import Model

import json

print('loading model...')

try:
    model = Model('./model/ggml-gpt4all-j')

except:
    print("An exception occurred on loading model.")

print('model loaded\n')

default_params: dict = {
    "seed": -1,
    "n_threads": -1,
    "n_predict": 200,
    "top_k": 40,
    "top_p": 0.9,
    "temp": 0.9,
    "repeat_penalty": 1,
    "repeat_last_n": 64,
    "n_batch":  8
}


def handler(event, context):
    body = {
        "message": "OK",
    }

    if event.get("source") == "serverless-plugin-warmup":
        body['message'] = 'WarmUP - Keep the Lambda warm!'

    else:
        data = json.loads(event['body'])
        print("prompt", data['prompt'])
        if 'params' in data:
            print("params", data['params'])
            default_params.update(data['params'])
            print("updated default_params", default_params)
        result = model.generate(
            prompt=data['prompt'],
            seed=default_params["seed"],
            n_threads=default_params["n_threads"],
            n_predict=default_params["n_predict"],
            top_k=default_params["top_k"],
            top_p=default_params["top_p"],
            temp=default_params["temp"],
            repeat_penalty=default_params["repeat_penalty"],
            repeat_last_n=default_params["repeat_last_n"],
            n_batch=default_params["n_batch"]
        )
        print(f"result: {result}")
        body = {
            "message": result,
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response
