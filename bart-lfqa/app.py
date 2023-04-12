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
        inputs = tokenizer(data['prompt'], truncation=True,
                           padding=True, return_tensors="pt")
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            min_length=64,
            max_length=256,
            do_sample=False,
            early_stopping=True,
            num_beams=8,
            temperature=1.0,
            top_k=None,
            top_p=None,
            eos_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            num_return_sequences=1)
        result = tokenizer.batch_decode(
            outputs, skip_special_tokens=True,
            clean_up_tokenization_spaces=True)
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
