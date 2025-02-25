import boto3
import os
import json

import boto3.dynamodb

def handler(event, context):
    tableName = os.getenv('TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    #this is actually the userid
    username = event['cognitoPoolClaims'].get('username', [])
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('Userid').eq(username)
    )
    items = response['Items']
    if(not items):
        return {
            'statusCode': 404,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
             },
            'body': json.dumps({'message': 'User not found'}),
        }
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
         },
        'body': json.dumps(items),
    }