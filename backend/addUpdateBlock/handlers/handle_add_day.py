import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_add_day(data, dbUtils, responseUtils):
    logger.info("Adding new day %s to week %s in block %s", data.get('newDayId'), data.get('weekId'), data.get('blockId'))
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
        
        # Check if day already exists in the map
        if data['newDayId'] in days:
            logger.error("Day %s already exists in week %s", data['newDayId'], data['weekId'])
            return responseUtils.error_response(400, f'Day {data["newDayId"]} already exists in this week')

        # Add new day to the map
        dbUtils.table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET #b.Weeks.#weekId.Days.#dayId = :new_day",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#dayId': data['newDayId'],
                '#b': 'Block'
            },
            ExpressionAttributeValues={
                ':new_day': {
                    'dayId': data['newDayId'],
                    'dayIndex': str(len(days)),
                    'Exercises': []
                }
            }
        )
        
        logger.info("Successfully added day %s", data['newDayId'])
        return responseUtils.success_response({
            'message': 'Day added',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['weekId'],
                'dayId': data['newDayId'],
                'timestamp': block['Timestamp']
            }
        })
    except Exception as e:
        logger.error("Error adding day: %s", str(e))
        return responseUtils.error_response(500, str(e))
