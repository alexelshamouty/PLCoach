
import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_add_week(table, data, get_block_by_name, error_response, success_response):
    logger.info("Adding new week %s to block %s for user %s", data.get('newWeekId'), data.get('blockId'), data.get('userId'))
    try:
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        weeks = block.get('Block', {}).get('Weeks', {})
        
        # Check if week already exists
        if data['newWeekId'] in weeks:
            logger.error("Week %s already exists in block %s", data['newWeekId'], data['blockId'])
            return error_response(400, f'Week {data["newWeekId"]} already exists in this block')

        # Add new week using the block's Timestamp
        table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']  # Use the actual Timestamp from the block
            },
            UpdateExpression="SET #b.Weeks.#weekId = :weekData",
            ExpressionAttributeNames={
                '#weekId': data['newWeekId'],
                '#b': 'Block'
            },
            ExpressionAttributeValues={
                ':weekData': {
                    'Days': {}, #Makes our live easier. We need something ordered.
                    'WeekNumber': data['newWeekId']
                }
            }
        )
        
        logger.info("Successfully added week %s to block %s", data['newWeekId'], data['blockId'])
        return success_response({
            'message': 'Week added',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['newWeekId'],
                'timestamp': block['Timestamp']
            }
        })
    except Exception as e:
        logger.error("Error adding week: %s", str(e))
        return error_response(500, str(e))
