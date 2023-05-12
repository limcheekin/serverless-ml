from gpt4allj import Model
import json
import multiprocessing
import copy

print('loading model...')
cpu_count = multiprocessing.cpu_count()
print("cpu_count", cpu_count)
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
    "temperature": 0.9,
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
        params = copy.deepcopy(default_params)
        data = json.loads(event['body'])
        print("prompt", data['prompt'])
        if 'params' in data:
            print("params", data['params'])
            params.update(data['params'])
            print("updated params", params)
            if params['n_threads'] == -1:
                params['n_threads'] = cpu_count
        result = model.generate(
            prompt=data['prompt'],
            seed=params["seed"],
            n_threads=params["n_threads"],
            n_predict=params["n_predict"],
            top_k=params["top_k"],
            top_p=params["top_p"],
            temp=params["temperature"],
            repeat_penalty=params["repeat_penalty"],
            repeat_last_n=params["repeat_last_n"],
            n_batch=params["n_batch"]
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
