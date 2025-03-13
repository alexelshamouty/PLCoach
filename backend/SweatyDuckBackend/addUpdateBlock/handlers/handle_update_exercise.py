import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_update_exercise(data, dbUtils, responseUtils):
    logger.info("Updating exercise results in day %s in week %s of block %s", data.get('dayId'), data.get('weekId'), data.get('blockId'))
    try:
        # Validate required fields
        required_fields = {
            'userId': str,
            'blockId': str,
            'weekId': str,
            'dayId': str,
            'exerciseName': str,
            'sets': list,
            'comments': str
        }
        
        for field, field_type in required_fields.items():
            if field not in data:
                logger.error("Missing required field: %s", field)
                return responseUtils.error_response(400, f"Missing required field: {field}")
            if not isinstance(data[field], field_type):
                logger.error("Invalid type for field %s, expected %s", field, field_type)
                return responseUtils.error_response(400, f"Invalid type for field {field}")

        # Get block
        block, error = dbUtils.get_block_by_name(data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        # Navigate to the specific exercise
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        if not week:
            logger.error("Week %s not found in block %s", data['weekId'], data['blockId'])
            return responseUtils.error_response(404, f"Week {data['weekId']} not found in block {data['blockId']}")
            
        days = week.get('Days', {})
        if data['dayId'] not in days:
            logger.error("Day %s not found in week %s", data['dayId'], data['weekId'])
            return responseUtils.error_response(404, f"Day {data['dayId']} not found in week {data['weekId']}")

        exercises = days[data['dayId']].get('Exercises', [])
        exercise_index = next((i for i, e in enumerate(exercises) 
                             if e['name'] == data['exerciseName']), -1)

        if exercise_index == -1:
            logger.error("Exercise not found: %s", data['exerciseName'])
            return responseUtils.error_response(404, 'Exercise not found')

        # Create the results entry
        results_entry = {
            'sets': data['sets'],
            'comments': data['comments']
        }

        # Update the exercise's results
        exercise_path = f"#b.Weeks.#weekId.Days.#dayId.Exercises[{exercise_index}].results"
        
        dbUtils.table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression=f"SET {exercise_path} = :results",
            ExpressionAttributeNames={
                '#b': 'Block',
                '#weekId': data['weekId'],
                '#dayId': data['dayId']
            },
            ExpressionAttributeValues={
                ':results': results_entry
            }
        )

        logger.info("Successfully updated exercise results")
        return responseUtils.success_response({
            'message': 'Exercise results updated',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['weekId'],
                'dayId': data['dayId'],
                'exerciseName': data['exerciseName']
            }
        })
        
    except Exception as e:
        logger.error("Error updating exercise: %s", str(e))
        return responseUtils.error_response(500, f"Internal server error: {str(e)}")
