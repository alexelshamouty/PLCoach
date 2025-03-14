import os
import logging
from utils.response_utils import ResponseUtils
from utils.db_utils import DBUtils
from handlers import (handle_get_all_blocks, handle_get_days_by_week)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
            
def handler(event, context):
    # Handle warmup event
    if event.get("source") == "serverless-plugin-warmup":
        logger.info("WarmUp event")
        return {}
    
    logger.info("Handler started with event: %s", event)
    tableName = os.getenv('BLOCK_TABLE_NAME')
    
    action_handlers = {
        'getAllBlocks': handle_get_all_blocks,
        'getDaysByWeek': handle_get_days_by_week
    }

    responseUtils = ResponseUtils(None)
    dbUtils = DBUtils(tableName)

    logger.info(f"Handler started with event: {event}")
    #TODO: This needs to allow the user to retreive their information too. But not now we need to finish the admin functionality
    #TODO: Yes this is bad and we need to change it but first the functionality
    auth_response_admin = responseUtils.authorize(event,['coaches','athletes'])
    if auth_response_admin:
        logger.error("Not an admin")
        return auth_response_admin

    try:
        # Parse query parameters
        query_params = event.get('queryStringParameters', {})
        if not query_params:
            logger.error("Missing query parameters")
            return responseUtils.error_response(400, "Missing query parameters")

        action = query_params.get('action')
        if not action:
            logger.error("Missing action parameter")
            return responseUtils.error_response(400, "Missing action parameter")

        if action not in ['getBlockByName', 'getAllBlocks','getDaysByWeek']:
            logger.error("Invalid action: %s", action)
            return responseUtils.error_response(400, "Invalid action. Must be 'getBlockByName' or 'getAllBlocks'")

        user_id = query_params.get('userId')
        if not user_id:
            logger.error("Missing userId parameter")
            return responseUtils.error_response(400, "Missing userId parameter")


        handler = action_handlers.get(action)
        if handler:
            return handler(query_params, dbUtils, responseUtils)
        return responseUtils.error_response(400, f"Unknown action {action}")
    except Exception as e:
        logger.error("Error processing request: %s", str(e))
        return responseUtils.error_response(500, f"Internal server error: {str(e)}")

