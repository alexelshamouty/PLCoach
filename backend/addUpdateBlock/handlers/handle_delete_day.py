import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_delete_day(data, dbUtils, responseUtils):
    logger.info("Deleting day %s from week %s in block %s", data.get('dayId'), data.get('weekId'), data.get('blockId'))
    try:
        block, error = dbUtils.get_block_by_name(data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        
        if not week:
            logger.error("Week %s not found in block %s", data['weekId'], data['blockId'])
            return responseUtils.error_response(404, 'Week not found')
            
        days = week.get('Days', {})
        
        # Check if the day exists in the map
        if data['dayId'] not in days:
            logger.error("Day %s not found in week %s", data['dayId'], data['weekId'])
            return responseUtils.error_response(404, f'Day {data["dayId"]} not found in this week')

        # Remove the day from the map
        dbUtils.table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="REMOVE #b.Weeks.#weekId.Days.#dayId",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#dayId': data['dayId'],
                '#b': 'Block'
            }
        )
        
        logger.info("Successfully deleted day %s", data['dayId'])
        return responseUtils.success_response({
            'message': 'Day deleted',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['weekId'],
                'dayId': data['dayId'],
                'timestamp': block['Timestamp']
            }
        })
    except Exception as e:
        logger.error("Error deleting day: %s", str(e))
        return responseUtils.error_response(500, str(e))
