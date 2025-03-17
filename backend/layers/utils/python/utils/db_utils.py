from boto3.dynamodb.conditions import Key
import boto3
from .response_utils import ResponseUtils
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
                return None, self.responseUtils.error_response(404, f'Block with name {block_name} not found')
                
            return response['Items'][0], None
            
        except Exception as e:
            return None, self.responseUtils.error_response(500, f'Error querying block: {str(e)}')
        
    def save_template(self, template):
        """
        Save a template to the database
        Returns error_response if there was an error, or None if successful
        """
        try:
            item = {
                "TemplateName": template["templateName"],  
                "metrics": template["metrics"]
            }
            logger.info(f"Saving a new template {item}")
            template_exists = self.get_template_by_name(item["TemplateName"])
            
            if template_exists:
                return self.responseUtils.error_response(409, f'Template with name {item["TemplateName"]} already exists')
                        
            self.table.put_item(Item=item)
            return None
        except Exception as e:
            logger.error(f"Error saving template: {str(e)}")
            return self.responseUtils.error_response(500, f'Error saving template: {str(e)}')
        
    def update_template(self, template):
        """
        Update a template in the database
        Returns error_response if there was an error, or None if successful
        """
        try:
            item = {
                "TemplateName": template["templateName"],
                "metrics": template["metrics"]
            }
            self.table.put_item(Item=item)
            return None
        except Exception as e:
            return self.responseUtils.error_response(500, f'Error updating template: {str(e)}')
        
    def get_templates(self):
        """
        Get all templates from the database
        Returns (templates, error_response)
        If successful: returns (templates, None)
        If error: returns (None, error_response)
        """
        try:
            response = self.table.scan()
            return response['Items'], None
        except Exception as e:
            return None, self.responseUtils.error_response(500, f'Error querying templates: {str(e)}')
        
    def get_template_by_name(self, template_name):
        """
        Get a template by its name
        Returns template if found, None if not found
        """
        try:
            response = self.table.query(
                KeyConditionExpression=Key('TemplateName').eq(template_name)
            )
            
            if len(response['Items']) == 0:
                return None
                
            return response['Items'][0]
            
        except Exception as e:
            logger.error(f"Error querying template: {str(e)}")
            return None