import json
import base64
import tempfile
#import keras.applications
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np

#keras.applications.imagenet_utils.CLASS_INDEX = json.load(open('imagenet_class_index.json'))

print('loading model...')

try:
  model = ResNet50(weights='resnet50_weights_tf_dim_ordering_tf_kernels.h5')
except:
  print("An exception occurred on loading model.")

print('model loaded\n')

# REF: https://stackoverflow.com/questions/46098047/how-to-fetch-get-and-post-params-inside-a-aws-lambda-function
# With the Lambda proxy integration, API Gateway maps the entire client request to the
# input event parameter of the backend Lambda function as follows:
# {
#     "resource": "Resource path",
#     "path": "Path parameter",
#     "httpMethod": "Incoming request's method name"
#     "headers": {Incoming request headers}
#     "queryStringParameters": {query string parameters }
#     "pathParameters":  {path parameters}
#     "stageVariables": {Applicable stage variables}
#     "requestContext": {Request context, including authorizer-returned key-value pairs}
#     "body": "A JSON string of the request payload."
#     "isBase64Encoded": "A boolean flag to indicate if the applicable request payload is Base64-encode"
# }
def handler(event, context):
    body = {
        "message": "OK",
    }

    if event.get("source") == "serverless-plugin-warmup":
      body['message'] = 'WarmUP - Keep the Lambda warm!'

    else: 
      # REF: https://medium.com/@shresthshruti09/image-upload-on-aws-s3-using-api-gateway-and-lambda-in-python-4039276b7ca7
      data = json.loads(event['body'])
      print("data['name']", data['name'])
      file_content = base64.b64decode(data['file'])
      # REF: https://stackoverflow.com/questions/11043372/how-to-use-tempfile-namedtemporaryfile
      tmp_image_file = tempfile.NamedTemporaryFile()
      tmp_image_file.write(file_content)
      print('tmp_image_file.name', tmp_image_file.name)

      img = image.load_img(tmp_image_file.name, target_size=(224, 224))
      tmp_image_file.close()
      x = image.img_to_array(img)
      x = np.expand_dims(x, axis=0) 
      x = preprocess_input(x)
      
      # predict image classes and decode predictions
      predictions = model.predict(x)
      decoded_predictions = decode_predictions(predictions, top=3)[0]
      predictions_list = []
      for pred in decoded_predictions:
          predictions_list.append({'label': pred[1].replace('_', ' ').capitalize(), 'probability': float(pred[2])})

      body['predictions'] = predictions_list

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        }
    }

    return response