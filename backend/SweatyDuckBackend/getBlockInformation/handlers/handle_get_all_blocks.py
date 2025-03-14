import logging
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_get_all_blocks(query_params, dbUtils, responseUtils):
    user_id = query_params.get('userId')
    logger.info("Processing getAllBlocks request for userId: %s", user_id)
    
    # Query blocks for user, sorted by timestamp descending
    response = dbUtils.table.query(
        KeyConditionExpression=Key('Userid').eq(user_id),
        ProjectionExpression='BlockName, #b.Weeks, #ts',
        ExpressionAttributeNames={
            '#ts': 'Timestamp',
            '#b': 'Block'
        },
        ScanIndexForward=False  # this will sort by timestamp descending (newest first)
    )
    
    if not response.get('Items'):
        return responseUtils.success_response({'blocks': {}})
        
    # Transform the response into a map of blocknames with their weeks
    blocks_map = {}
    for item in response['Items']:
        blocks_map[item['BlockName']] = list(item.get('Block', {}).get('Weeks', {}).keys())
        
    return responseUtils.success_response({
        'blocks': blocks_map
    })