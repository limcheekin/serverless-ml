print('container start')

#try:
#    import unzip_requirements
#except ImportError as error:
#    print(error)

#print('unzipped')

import json
import spacy
from os import walk

d = []
for (dirpath, dirnames, filenames) in walk('/var/task/'):
    d.extend(dirnames)
    break
print("directories", d)
#import en_core_web_sm

#MODEL = en_core_web_sm.load()
MODEL = spacy.load('en_core_web_sm')
#MODEL = spacy.load('/var/task/en_core_web_sm/en_core_web_sm-3.0.0')
# REF: https://github.com/keithrozario/Klayers/issues/97
#MODEL = spacy.load("/opt/en_core_web_sm-2.2.5/en_core_web_sm/en_core_web_sm-2.2.5")
print('model loaded')

def create_ner_spans(text):
    doc = MODEL(text)
    spans = []
    for ent in doc.ents:
        span = {
            'start': ent.start_char,
            'end': ent.end_char,
            'type': ent.label_
        }
        spans.append(span)
    return spans


def handler(event, context):
    body = {
        "message": "OK",
    }

    if event.get("source") == "serverless-plugin-warmup":
        body['message'] = 'WarmUP - Keep the Lambda warm!'

    else:
        text = event['body']
        print(text)
        spans = []
        if text is not None:
            spans = create_ner_spans(text)
        print(spans)

        body = {
            'spans': spans
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    return response

def do_main():
    event = {
        'source': 'main',
        'body': 'Jim bought 300 shares of Acme Corp. in 2006.',
    }

    response = handler(event, None)
    body = json.loads(response['body'])
    print('body:', body)

    

#do_main()    