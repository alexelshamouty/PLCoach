import boto3
import os
import logging
import boto3.dynamodb

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Event received: %s", event)
    tableName = os.getenv('TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)

    # Get userId from query parameters
    # TODO: We need to move to lambda-proxy 
    query_params = event.get('query', {})
    logger.info("Query parameters: %s", query_params)
    userId = query_params.get('userId') if query_params else None
    
    if not userId:
        logger.error("Missing userId parameter")
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'body': {'message': 'Missing userId parameter'}
        }

    logger.info("Querying for userId: %s", userId)
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('Userid').eq(userId)
    )
    items = response['Items']
    
    if not items:
        logger.warning("No items found for userId: %s", userId)
        return {
            'statusCode': 404,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'body': {'message': 'User not found'}
        }
    
    logger.info("Found items: %s", items)    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': items
    }