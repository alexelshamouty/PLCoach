import boto3
import os
import json
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    # Handle warmup event
    if event.get("source") == "serverless-plugin-warmup":
        logger.info("WarmUp event")
        return {}
    tableName = os.getenv('TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    groups = event['cognitoPoolClaims'].get('groups', [])
    if 'coaches' not in groups:
        print("Unauthorized user")
        print(event)
        return {
            'statusCode': 403,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Unauthorized'})
        }
    response = table.scan()
    items = response['Items']
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
         },
        'body': items
    }