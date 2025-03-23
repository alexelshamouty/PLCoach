import os
import json
import logging

from utils.response_utils import ResponseUtils
from utils.db_utils import DBUtils
from handlers import (handle_add_block, handle_add_week, handle_add_day, 
                      handle_add_exercise, handle_delete_exercise, handle_update_exercise)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# We are going to move to Magnum and FastAPi. All of this will be replaced by FastAPI
tableName = os.getenv('BLOCK_TABLE_NAME')

def handler(event, context):
    # Handle warmup event
    databaseUtils = DBUtils(tableName)
    responseUtils = ResponseUtils(logger)

    if event.get("source") == "serverless-plugin-warmup":
        logger.info("WarmUp event")
        return responseUtils.success_response({'message': 'Warmup request handled successfully'})
    
    logger.info("Handler started with event: %s", event)

    auth_response = responseUtils.authorize(event,['coaches','athletes'])
    if auth_response:
        logger.error("Authorization failed")
        return auth_response

    try:
        if 'body' not in event:
            logger.error("Missing request body")
            return responseUtils.error_response(400, 'Missing request body')
        
        if isinstance(event['body'], str):
            post_data = json.loads(event['body'])
        else:
            post_data = event['body']
            
        action = post_data.get('action')
        
        if not action:
            logger.error("Missing action parameter")
            return responseUtils.error_response(400, 'Missing action parameter')
            
        logger.info("Processing action: %s", action)

        # Map of actions to their handler functions
        action_handlers = {
            'addBlock': handle_add_block,
            'addWeek': handle_add_week,
            'addDay': handle_add_day,
            'addExercise': handle_add_exercise,
            'deleteExercise': handle_delete_exercise,
            'updateExercise': handle_update_exercise
        }

        handler = action_handlers.get(action)
        if handler:
            return handler(post_data, databaseUtils, responseUtils)
        
        logger.error("Unknown action: %s", action)
        return responseUtils.error_response(400, f'Unknown action: {action}')
            
    except json.JSONDecodeError:
        logger.error("Invalid JSON in request body")
        return responseUtils.error_response(400, 'Invalid JSON in request body')

