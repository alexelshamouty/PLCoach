import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_delete_exercise(data, dbUtils, responseUtils):
    logger.info("Deleting exercise from day %s in week %s of block %s", data.get('dayId'), data.get('weekId'), data.get('blockId'))
    try:
        # Validate required fields
        required_fields = {
            'userId': str,
            'blockId': str,
            'weekId': str,
            'dayId': str,
            'exerciseName': str,
            'exerciseLabel': str
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                logger.error("Missing required field: %s", field)
                return responseUtils.error_response(400, f"Missing required field: {field}")
            if not isinstance(data[field], field_type):
                logger.error("Invalid type for field %s, expected %s", field, field_type)
                return responseUtils.error_response(400, f"Invalid type for field {field}")

        block, error = dbUtils.get_block_by_name(data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        if not week:
            logger.error("Week %s not found in block %s", data['weekId'], data['blockId'])
            return responseUtils.error_response(404, f"Week {data['weekId']} not found in block {data['blockId']}")
            
        days = week.get('Days', {})
        if data['dayId'] not in days:
            logger.error("Day %s not found in week %s", data['dayId'], data['weekId'])
            return responseUtils.error_response(404, f"Day {data['dayId']} not found in week {data['weekId']}")
        
        # Find and remove the exercise
        exercises = days[data['dayId']].get('Exercises', [])
        exercise_index = next((i for i, e in enumerate(exercises) 
                             if e['name'] == data['exerciseName'] 
                             and e['label'] == data['exerciseLabel']), -1)
        
        if exercise_index == -1:
            logger.error("Exercise not found: %s with label %s", data['exerciseName'], data['exerciseLabel'])
            return responseUtils.error_response(404, 'Exercise not found')

        # Update with new exercises list excluding the removed exercise
        dbUtils.table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET #b.Weeks.#weekId.Days.#dayId.Exercises = :exercises",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#dayId': data['dayId'],
                '#b': 'Block'
            },
            ExpressionAttributeValues={
                ':exercises': [e for i, e in enumerate(exercises) if i != exercise_index]
            }
        )
        
        logger.info("Successfully deleted exercise from day %s", data['dayId'])
        return responseUtils.success_response({
            'message': 'Exercise deleted',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['weekId'],
                'dayId': data['dayId'],
                'exerciseName': data['exerciseName'],
                'exerciseLabel': data['exerciseLabel']
            }
        })
    except Exception as e:
        logger.error("Error deleting exercise: %s", str(e))
        return responseUtils.error_response(500, f"Internal server error: {str(e)}")
