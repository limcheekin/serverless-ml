from llama_cpp import Llama
import json
import multiprocessing

print('loading model...')
cpu_count = multiprocessing.cpu_count()
print("cpu_count", cpu_count)
try:
    llm = Llama(
        model_path="./model/redpajama-chat-3b-v1-ggml-model-q4_2.bin",
        n_ctx=2048,
        use_mlock=True, 
        n_threads=cpu_count
    )
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
        result = llm(data['prompt'], max_tokens=256,
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
