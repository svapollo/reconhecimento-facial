import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def detecta_faces():
    faces_detectadas = client.index_faces(
        CollectionId='personagem',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': 'comparar',
                'Name': 'tres.jpg',
            },
        },
    )
    return faces_detectadas


faces_detectadas = detecta_faces()
print(json.dumps(faces_detectadas, indent=4))
