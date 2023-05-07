from llama_cpp import Llama
import json

print('loading model...')

try:
    llm = Llama(model_path="./model/openllama-7b-300bt-ggml-q4_0.bin")
except:
    print("An exception occurred on loading model.")

print('model loaded\n')


def handler(event, context):
    body = {
        "message": "OK",
    }

    if event.get("source") == "serverless-plugin-warmup":
        body['message'] = 'WarmUP - Keep the Lambda warm!'

    else:
        data = json.loads(event['body'])
        print("data['prompt']", data['prompt'])
        result = llm(data['prompt'], max_tokens=32,
                     stop=["Q:", "\n"], echo=True)
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
