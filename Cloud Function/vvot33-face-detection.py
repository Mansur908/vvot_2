import boto3
import io
import requests
import base64
import json
import os

def handler(event, context):
    
    session = boto3.session.Session(region_name='ru-central1')
    s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net')
    bucket_id = event['messages'][0]['details']['bucket_id']
    object_id = event['messages'][0]['details']['object_id']
    photo_object = io.BytesIO()
    s3.download_fileobj(bucket_id, object_id, photo_object)
    photo = base64.b64encode(photo_object.getvalue())
    token = context.token['access_token'] 
    headers = {'Authorization': 'Bearer ' + token}
    vision_url = 'https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze'
    
    data = {
    "analyze_specs": [{
        "content": str(photo)[2:-1],
        "features": [{
            "type": "FACE_DETECTION"
        }]
    }]
    }

    r = requests.post(
        url = vision_url,
        headers = headers,
        data = str(data))

    print(r.text)

    data = json.loads(r.text)
    
    client = boto3.client(
        service_name='sqs',
        endpoint_url='https://message-queue.api.cloud.yandex.net',
        region_name='ru-central1'
    )

    for i in data['results'][0]['results'][0]['faceDetection']['faces']:
        client.send_message(
            QueueUrl = os.getenv('QueueUrl'),
            MessageBody = "{" + f"\"photo\": \"{object_id}\", \"coordinates\": {i['boundingBox']['vertices']}" + "}"
        )

    return {
        'statusCode': 200,
        'body': ''
    }
