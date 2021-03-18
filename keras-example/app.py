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

def handler(event, context):
    body = {}

    # REF: https://medium.com/swlh/upload-binary-files-to-s3-using-aws-api-gateway-with-aws-lambda-2b4ba8c70b8e
    file_content = base64.b64decode(event['content'])
    
    tmp_image_file = tempfile.TemporaryFile()
    tmp_image_file.write(file_content)
    print(tmp_image_file.name)

    img = image.load_img(tmp_image_file.name, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) 
    x = preprocess_input(x)
    tmp_image_file.close()
    
    # predict image classes and decode predictions
    predictions = model.predict(x)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    predictions_list = []
    for pred in decoded_predictions:
        predictions_list.append({'label': pred[1].replace('_', ' ').capitalize(), 'probability': float(pred[2])})

    body['message'] = 'OK'
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