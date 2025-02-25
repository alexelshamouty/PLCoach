import boto3
import os

def handler(event, context):
    tableName = os.getenv('TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)

    response = table.scan()
    items = response['Items']

    return {
        'statusCode': 200,
        'body': items,
        'content-type': 'application/json'
    }