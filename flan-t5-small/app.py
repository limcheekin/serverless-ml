from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import json

print('loading model...')

try:
    model = AutoModelForSeq2SeqLM.from_pretrained("model/")
    tokenizer = AutoTokenizer.from_pretrained("model/")
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
        inputs = tokenizer(data['prompt'], return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=200)
        result = tokenizer.batch_decode(outputs, skip_special_tokens=True))
        print(f"result: {result}")
        body={
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
