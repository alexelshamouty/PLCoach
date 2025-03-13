
import boto3
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_update_exercise(table, data, get_block_by_name, error_response, success_response):
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
                return error_response(400, f"Missing required field: {field}")
            if not isinstance(data[field], field_type):
                logger.error("Invalid type for field %s, expected %s", field, field_type)
                return error_response(400, f"Invalid type for field {field}")

        # Get block
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        # Navigate to the specific exercise
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        if not week:
            logger.error("Week %s not found in block %s", data['weekId'], data['blockId'])
            return error_response(404, 'Week not found')
            
        days = week.get('Days', {})
        if data['dayId'] not in days:
            logger.error("Day %s not found in week %s", data['dayId'], data['weekId'])
            return error_response(404, 'Day not found')

        exercises = days[data['dayId']].get('Exercises', [])
        exercise_index = next((i for i, e in enumerate(exercises) 
                             if e['name'] == data['exerciseName']), -1)

        if exercise_index == -1:
            logger.error("Exercise not found: %s", data['exerciseName'])
            return error_response(404, 'Exercise not found')

        # Create the results entry
        results_entry = {
            'sets': data['sets'],
            'comments': data['comments']
        }

        # Update the exercise's results
        exercise_path = f"#b.Weeks.#weekId.Days.#dayId.Exercises[{exercise_index}].results"
        
        table.update_item(
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
        return success_response({
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
        return error_response(500, str(e))
