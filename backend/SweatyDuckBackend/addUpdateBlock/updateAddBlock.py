import boto3
import os
import json
import datetime
import logging
from boto3.dynamodb.conditions import Key
from utils.response_utils import error_response, success_response, authorize
from utils.db_utils import get_block_by_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Handler started with event: %s", event)
    tableName = os.getenv('BLOCK_TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    
    auth_response = authorize(event)
    if auth_response:
        logger.error("Authorization failed")
        return auth_response

    try:
        if 'body' not in event:
            logger.error("Missing request body")
            return error_response(400, 'Missing request body')
        
        if isinstance(event['body'], str):
            post_data = json.loads(event['body'])
        else:
            post_data = event['body']
            
        action = post_data.get('action')
        
        if not action:
            logger.error("Missing action parameter")
            return error_response(400, 'Missing action parameter')
            
        logger.info("Processing action: %s", action)
        # Command selector
        if action == 'addBlock':
            return handle_add_block(table, post_data)
        elif action == 'addWeek':
            return handle_add_week(table, post_data)
        elif action == 'addDay':
            return handle_add_day(table, post_data)
        elif action == 'addExercise':
            return handle_add_exercise(table, post_data)
        else:
            logger.error("Unknown action: %s", action)
            return error_response(400, f'Unknown action: {action}')
            
    except json.JSONDecodeError:
        logger.error("Invalid JSON in request body")
        return error_response(400, 'Invalid JSON in request body')

def handle_add_block(table, data):
    logger.info("Adding new block with name: %s for user: %s", data.get('blockName'), data.get('user_id'))
    try:
        # Check if block already exists using common method
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

def handle_add_week(table, data):
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
                    'Days': {},
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

def handle_add_day(table, data):
    logger.info("Adding new day %s to week %s in block %s", data.get('newDayId'), data.get('weekId'), data.get('blockId'))
    try:
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        
        # We kinda do not need to do that but this is very cheap to do since the data is already in memory
        # This makes error handeling nicer to the frontend rather than just sending a 500 error
        # 500 errors should be kept for things we don't know why the failed.
        if not week:
            logger.error("Week %s not found in block %s", data['weekId'], data['blockId'])
            return error_response(404, 'Week not found')
            
        # Initialize days as a list if it doesn't exist
        days = week.get('Days', [])
        
        # Check if day already exists in the list
        if any(day['dayId'] == data['newDayId'] for day in days):
            logger.error("Day %s already exists in week %s", data['newDayId'], data['weekId'])
            return error_response(400, f'Day {data["newDayId"]} already exists in this week')

        # Add new day to the list
        table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET #b.Weeks.#weekId.Days = list_append(if_not_exists(#b.Weeks.#weekId.Days, :empty_list), :new_day)",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#b': 'Block'
            },
            ExpressionAttributeValues={
                ':empty_list': [],
                ':new_day': [{
                    'dayId': data['newDayId'],
                    'Exercises': [],
                    'dayNumber': len(days) + 1  # Add day number for ordering
                }]
            }
        )
        
        logger.info("Successfully added day %s", data['newDayId'])
        return success_response({
            'message': 'Day added',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['weekId'],
                'dayId': data['newDayId'],
                'dayNumber': len(days) + 1,
                'timestamp': block['Timestamp']
            }
        })
    except Exception as e:
        logger.error("Error adding day: %s", str(e))
        return error_response(500, str(e))

def handle_add_exercise(table, data):
    logger.info("Adding new exercise to day %s in week %s of block %s", data.get('dayId'), data.get('weekId'), data.get('blockId'))
    try:
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            logger.error("Error retrieving block: %s", error)
            return error
            
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        
        if not week:
            logger.error("Week %s not found in block %s", data['weekId'], data['blockId'])
            return error_response(404, 'Week not found')
            
        days = week.get('Days', [])
        day = next((d for d in days if d['dayId'] == data['dayId']), None)
        
        if not day:
            logger.error("Day %s not found in week %s", data['dayId'], data['weekId'])
            return error_response(404, 'Day not found')

        # Add new exercise to the list
        table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET #b.Weeks.#weekId.Days[#dayIndex].Exercises = list_append(if_not_exists(#b.Weeks.#weekId.Days[#dayIndex].Exercises, :empty_list), :new_exercise)",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#dayIndex': str(days.index(day)),
                '#b': 'Block'
            },
            ExpressionAttributeValues={
                ':empty_list': [],
                ':new_exercise': [data['exercise']]
            }
        )
        
        logger.info("Successfully added exercise to day %s", data['dayId'])
        return success_response({
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
        return error_response(500, str(e))