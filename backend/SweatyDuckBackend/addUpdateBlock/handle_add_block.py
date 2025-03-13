import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_add_block(table, data, get_block_by_name, error_response, success_response):
    logger.info("Adding new block with name: %s for user: %s", data.get('blockName'), data.get('user_id'))
    try:
        # Check if block already exists using injected method
        block, error = get_block_by_name(table, data['user_id'], data['blockName'])
        
        if block:
            logger.warning("Block already exists: %s", data['blockName'])
            return error_response(400, f'Block with name {data["blockName"]} already exists')

        # Create new block with current timestamp
        current_time = datetime.datetime.now().isoformat()
        
        table.put_item(
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
        return success_response({
            'message': 'Block added',
            'data': {
                'userId': data['user_id'],
                'timestamp': current_time,
                'blockName': data['blockName']
            }
        })
    except Exception as e:
        logger.error("Error adding block: %s", str(e))
        return error_response(500, str(e))