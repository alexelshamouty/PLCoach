import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_add_block(data, dbUtils, responseUtils):
    logger.info("Adding new block with name: %s for user: %s", data.get('blockName'), data.get('user_id'))
    try:
        # Check if block already exists using injected method
        block, error = dbUtils.get_block_by_name(data['user_id'], data['blockName'])
        
        if block:
            logger.warning("Block already exists: %s", data['blockName'])
            return responseUtils.error_response(400, f'Block with name {data["blockName"]} already exists')

        # Create new block with current timestamp
        current_time = datetime.datetime.now().isoformat()
        
        responseUtils.table.put_item(
            Item={
                'Userid': data['user_id'],
                'Timestamp': current_time,
                'BlockName': data['blockName'],
                'Block': {
                    'Weeks': {}
                }
            }
        )
        
        logger.info("Successfully added block: %s", data['blockName'])
        return responseUtils.success_response({
            'message': 'Block added',
            'data': {
                'userId': data['user_id'],
                'timestamp': current_time,
                'blockName': data['blockName']
            }
        })
    except Exception as e:
        logger.error("Error adding block: %s", str(e))
        return responseUtils.error_response(500, str(e))