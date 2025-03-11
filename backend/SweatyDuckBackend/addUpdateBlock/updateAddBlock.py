import boto3
import os
import json
import datetime
from boto3.dynamodb.conditions import Key
from utils.response_utils import error_response, success_response, authorize
from utils.db_utils import get_block_by_name

def handler(event, context):
    tableName = os.getenv('TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    
    # Check authorization
    auth_response = authorize(event)
    if auth_response:
        return auth_response

    try:
        if 'body' not in event:
            return error_response(400, 'Missing request body')
        
        post_data = json.loads(event['body'])
        action = post_data.get('action')
        
        if not action:
            return error_response(400, 'Missing action parameter')
            
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
            return error_response(400, f'Unknown action: {action}')
            
    except json.JSONDecodeError:
        return error_response(400, 'Invalid JSON in request body')

def handle_add_block(table, data):
    try:
        # Check if block already exists using common method
        block, error = get_block_by_name(table, data['user_id'], data['blockName'])
        
        if block:  # If block exists, return error
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
        
        return success_response({
            'message': 'Block added',
            'data': {
                'userId': data['user_id'],
                'timestamp': current_time,
                'blockName': data['blockName']
            }
        })
    except Exception as e:
        return error_response(500, str(e))

def handle_add_week(table, data):
    try:
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            return error
            
        weeks = block.get('Block', {}).get('Weeks', {})
        
        # Check if week already exists
        if data['newWeekId'] in weeks:
            return error_response(400, f'Week {data["newWeekId"]} already exists in this block')

        # Add new week using the block's Timestamp
        table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']  # Use the actual Timestamp from the block
            },
            UpdateExpression="SET Block.Weeks.#weekId = :weekData",
            ExpressionAttributeNames={
                '#weekId': data['newWeekId']
            },
            ExpressionAttributeValues={
                ':weekData': {
                    'Days': {},
                    'WeekNumber': data['newWeekId']
                }
            }
        )
        
        return success_response({
            'message': 'Week added',
            'data': {
                'blockName': data['blockId'],
                'weekId': data['newWeekId'],
                'timestamp': block['Timestamp']
            }
        })
    except Exception as e:
        return error_response(500, str(e))

def handle_add_day(table, data):
    try:
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            return error
            
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        
        # We kinda do not need to do that but this is very cheap to do since the data is already in memory
        # This makes error handeling nicer to the frontend rather than just sending a 500 error
        # 500 errors should be kept for things we don't know why the failed.
        if not week:
            return error_response(404, 'Week not found')
            
        # Initialize days as a list if it doesn't exist
        days = week.get('Days', [])
        
        # Check if day already exists in the list
        if any(day['dayId'] == data['newDayId'] for day in days):
            return error_response(400, f'Day {data["newDayId"]} already exists in this week')

        # Add new day to the list
        table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET Block.Weeks.#weekId.Days = list_append(if_not_exists(Block.Weeks.#weekId.Days, :empty_list), :new_day)",
            ExpressionAttributeNames={
                '#weekId': data['weekId']
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
        return error_response(500, str(e))

def handle_add_exercise(table, data):
    try:
        block, error = get_block_by_name(table, data['userId'], data['blockId'])
        if error:
            return error
            
        week = block.get('Block', {}).get('Weeks', {}).get(data['weekId'])
        
        if not week:
            return error_response(404, 'Week not found')
            
        days = week.get('Days', [])
        day = next((d for d in days if d['dayId'] == data['dayId']), None)
        
        if not day:
            return error_response(404, 'Day not found')

        # Add new exercise to the list
        table.update_item(
            Key={
                'Userid': data['userId'],
                'Timestamp': block['Timestamp']
            },
            UpdateExpression="SET Block.Weeks.#weekId.Days[#dayIndex].Exercises = list_append(if_not_exists(Block.Weeks.#weekId.Days[#dayIndex].Exercises, :empty_list), :new_exercise)",
            ExpressionAttributeNames={
                '#weekId': data['weekId'],
                '#dayIndex': str(days.index(day))
            },
            ExpressionAttributeValues={
                ':empty_list': [],
                ':new_exercise': [data['exercise']]
            }
        )
        
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
        return error_response(500, str(e))