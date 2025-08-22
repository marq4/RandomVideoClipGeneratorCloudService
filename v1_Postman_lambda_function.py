import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Event comes from APIGW as json.
    body = json.loads(event['body'])
    filename = body['file']
    num_clips = body['num_clips']
    min_duration = body['min_duration']
    max_duration = body['max_duration']

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        'body': json.dumps(f"Hello from Lambda! Values: {filename}, {num_clips}, {min_duration}, {max_duration}")
    }
#
