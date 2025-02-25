import boto3
import os
import json

def handler(event, context):
    tableName = os.getenv('TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    groups = event['cognitoPoolClaims'].get('cognito:groups', [])
    if 'coaches' not in groups:
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
        'body': json.dumps(items),
    }