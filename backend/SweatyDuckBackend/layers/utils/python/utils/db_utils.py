from boto3.dynamodb.conditions import Key
import boto3
from .response_utils import ResponseUtils
class DBUtils:
    def __init__(self, tableName):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(tableName)
        self.responseUtils = ResponseUtils(None)

    def get_block_by_name(self, user_id, block_name):
        """
        Get a block by its name and user ID
        Returns (block, error_response)
        If successful: returns (block, None)
        If error: returns (None, error_response)
        """
        try:
            response = self.table.query(
                KeyConditionExpression=Key('Userid').eq(user_id),
                FilterExpression='BlockName = :blockName',
                ExpressionAttributeValues={
                    ':blockName': block_name
                }
            )
            
            if not response['Items']:
                return None, error_response(404, f'Block with name {block_name} not found')
                
            return response['Items'][0], None
            
        except Exception as e:
            return None, error_response(500, f'Error querying block: {str(e)}')
