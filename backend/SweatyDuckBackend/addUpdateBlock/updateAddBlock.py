import boto3
import os
import json
import datetime
import logging
from boto3.dynamodb.conditions import Key
from utils.response_utils import error_response, success_response, authorize
from utils.db_utils import get_block_by_name

from handle_add_block import handle_add_block
from handle_add_week import handle_add_week
from handle_add_day import handle_add_day
from handle_add_exercise import handle_add_exercise
from handle_delete_exercise import handle_delete_exercise
from handle_update_exercise import handle_update_exercise

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    # Handle warmup event
    if event.get('warmup'):
        logger.info('Handling warmup request')
        return success_response({'message': 'Warmup request handled successfully'})

    logger.info("Handler started with event: %s", event)
    tableName = os.getenv('BLOCK_TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    
    auth_response = authorize(event)
    if auth_response:
        logger.error("Authorization failed")
        return auth_response

    try:
        if 'body' not in event:
            logger.error("Missing request body")
            return error_response(400, 'Missing request body')
        
        if isinstance(event['body'], str):
            post_data = json.loads(event['body'])
        else:
            post_data = event['body']
            
        action = post_data.get('action')
        
        if not action:
            logger.error("Missing action parameter")
            return error_response(400, 'Missing action parameter')
            
        logger.info("Processing action: %s", action)
        # Command selector
        if action == 'addBlock':
            return handle_add_block(table, post_data, get_block_by_name, error_response, success_response)
        elif action == 'addWeek':
            return handle_add_week(table, post_data, get_block_by_name, error_response, success_response)
        elif action == 'addDay':
            return handle_add_day(table, post_data, get_block_by_name, error_response, success_response)
        elif action == 'addExercise':
            return handle_add_exercise(table, post_data, get_block_by_name, error_response, success_response)
        elif action == 'deleteExercise':
            return handle_delete_exercise(table, post_data, get_block_by_name, error_response, success_response)
        elif action == 'updateExercise':
            return handle_update_exercise(table, post_data, get_block_by_name, error_response, success_response)
        else:
            logger.error("Unknown action: %s", action)
            return error_response(400, f'Unknown action: {action}')
            
    except json.JSONDecodeError:
        logger.error("Invalid JSON in request body")
        return error_response(400, 'Invalid JSON in request body')

