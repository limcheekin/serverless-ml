from llama_cpp import Llama
import json
import multiprocessing
import copy

print('loading model...')
cpu_count = multiprocessing.cpu_count()
print("cpu_count", cpu_count)
try:
    llm = Llama(
        model_path="./model/openllama-7b-300bt-ggml-q4_0.bin",
        n_ctx=2048,
        use_mlock=True, 
        n_threads=cpu_count
    )
except:
    print("An exception occurred on loading model.")

print('model loaded\n')

default_params: dict = {
    "max_tokens": 128,
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 40,
    "repeat_penalty": 1.1,
    "stop": []
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
        result = llm(data['prompt'], 
                     max_tokens=params['max_tokens'],
                     temperature=params['temperature'],
                     top_p=params['top_p'],
                     top_k=params['top_k'],
                     repeat_penalty=params['repeat_penalty'],
                     stop=params['stop']
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
