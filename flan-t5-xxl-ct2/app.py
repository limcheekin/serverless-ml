from transformers import AutoTokenizer
import ctranslate2
import json

print('loading model...')

try:
    translator = ctranslate2.Translator("google/flan-t5-xxl-ct2")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xxl-ct2")
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
        input_tokens = tokenizer.convert_ids_to_tokens(
            tokenizer.encode(data['prompt']))
        results = translator.translate_batch([input_tokens])
        output_tokens = results[0].hypotheses[0]
        result = tokenizer.decode(
            tokenizer.convert_tokens_to_ids(output_tokens))
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
