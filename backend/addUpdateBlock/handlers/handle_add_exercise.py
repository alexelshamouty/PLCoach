import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_add_exercise(data, dbUtils, responseUtils):
    logger.info("Adding new exercise to day %s in week %s of block %s", data.get('dayId'), data.get('weekId'), data.get('blockId'))
    try:
        # Validate required fields
        required_fields = {
            'userId': str,
            'blockId': str,
            'weekId': str,
            'dayId': str,
            'exercise': dict
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                logger.error("Missing required field: %s", field)
                return responseUtils.error_response(400, f"Missing required field: {field}")
            if not isinstance(data[field], field_type):
                logger.error("Invalid type for field %s, expected %s", field, field_type)
                return responseUtils.error_response(400, f"Invalid type for field {field}")

        # Validate exercise fields
        exercise = data['exercise']
        required_exercise_fields = {
            'name': str,
            'label': str,
            'sets': str,
            'reps': str,
            'rpe': str,
            'comments': str
        }
        
        for field, field_type in required_exercise_fields.items():
            if field not in exercise:
                logger.error("Missing required exercise field: %s", field)
                return responseUtils.error_response(400, f"Missing required exercise field: {field}")
            if not isinstance(exercise[field], field_type):
                logger.error("Invalid type for exercise field %s, expected %s", field, field_type)
                return responseUtils.error_response(400, f"Invalid type for exercise field {field}")

        # Continue with existing block retrieval and update logic
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
            return responseUtils.error_response(404, f"Day {data['dayId']} not found in week %s", data['weekId'])
        
        # Calculate dayIndex based on the number of existing exercises
        exercises = days[data['dayId']].get('Exercises', [])
        dayIndex = len(exercises)

        # Add empty results object and dayIndex to exercise
        exercise = data['exercise']
        exercise['results'] = {}
        exercise['dayIndex'] = str(dayIndex)

        dbUtils.table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET #b.Weeks.#weekId.Days.#dayId.Exercises = list_append(if_not_exists(#b.Weeks.#weekId.Days.#dayId.Exercises, :empty_list), :new_exercise)",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#dayId': data['dayId'],
                '#b': 'Block'
            },
            ExpressionAttributeValues={
                ':empty_list': [],
                ':new_exercise': [exercise]
            }
        )
        
        logger.info("Successfully added exercise to day %s with dayIndex %d", data['dayId'], dayIndex)
        return responseUtils.success_response({
            'message': 'Exercise added',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['weekId'],
                'dayId': data['dayId'],
                'exercise': data['exercise'],
                'timestamp': block['Timestamp']
            }
        })
    except Exception as e:
        logger.error("Error adding exercise: %s", str(e))
        return responseUtils.error_response(500, str(e))
