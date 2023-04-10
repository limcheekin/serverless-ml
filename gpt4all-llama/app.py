from pyllamacpp.model import Model
import json

print('loading model...')

try:
    model = Model(ggml_model="ggjt-model.bin", n_ctx=1024)
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
        result = model.generate(data['prompt'], n_predict=200)
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
