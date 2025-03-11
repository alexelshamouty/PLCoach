import boto3
import os
import json
import datetime
import logging
from boto3.dynamodb.conditions import Key
from utils.response_utils import error_response, success_response, authorize
from utils.db_utils import get_block_by_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Handler started with event: %s", event)
    tableName = os.getenv('BLOCK_TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    
    #TODO: This needs to allow the user to retreive their information too. But not now we need to finish the admin functionality
    auth_response = authorize(event)
    if auth_response:
        logger.error("Authorization failed")
        return auth_response

    try:
        # Parse query parameters
        query_params = event.get('queryStringParameters', {})
        if not query_params:
            logger.error("Missing query parameters")
            return error_response(400, "Missing query parameters")

        action = query_params.get('action')
        if not action:
            logger.error("Missing action parameter")
            return error_response(400, "Missing action parameter")

        if action not in ['getBlockByName', 'getAllBlocks']:
            logger.error("Invalid action: %s", action)
            return error_response(400, "Invalid action. Must be 'getBlockByName' or 'getAllBlocks'")

        user_id = query_params.get('userId')
        if not user_id:
            logger.error("Missing userId parameter")
            return error_response(400, "Missing userId parameter")

        if action == 'getBlockByName':
            block_id = query_params.get('blockId')
            if not block_id:
                logger.error("Missing blockId parameter for getBlockByName")
                return error_response(400, "Missing blockId parameter")
                
            logger.info("Processing getBlockByName request for blockId: %s, userId: %s", block_id, user_id)
            block, error = get_block_by_name(table, user_id, block_id)
            if error:
                return error
                
            if not block:
                return error_response(404, f"Block not found: {block_id}")
                
            return success_response({
                'block': block
            })
        elif action == 'getAllBlocks':
            logger.info("Processing getAllBlocks request for userId: %s", user_id)
            
            # Query blocks for user, sorted by timestamp descending
            response = table.query(
                KeyConditionExpression=Key('Userid').eq(user_id),
                ProjectionExpression='BlockName, #b.Weeks, #ts',
                ExpressionAttributeNames={
                    '#ts': 'Timestamp',
                    '#b': 'Block'
                },
                ScanIndexForward=False  # this will sort by timestamp descending (newest first)
            )
            
            if not response.get('Items'):
                return success_response({'blocks': {}})
                
            # Transform the response into a map of blocknames with their weeks
            blocks_map = {}
            for item in response['Items']:
                blocks_map[item['BlockName']] = list(item.get('Block', {}).get('Weeks', {}).keys())
                
            return success_response({
                'blocks': blocks_map
            })
            
    except Exception as e:
        logger.error("Error processing request: %s", str(e))
        return error_response(500, f"Internal server error: {str(e)}")

