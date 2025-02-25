import json
import boto3
import os
from datetime import datetime

import boto3.dynamodb

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    cognito = boto3.client('cognito-idp')
    tableName = os.getenv('TABLE_NAME', 'users')

    try:
        userAttributes = event['request']['userAttributes']
        userPoolId = event['userPoolId']
        region = event['region']
        userid = userAttributes['sub']
        username = event['userName']
        email = userAttributes['email']
        name = userAttributes['name']
        preferred_username = userAttributes['preferred_username']
        gender = userAttributes['gender']
        weight = userAttributes.get('custom:weight', '0')
        date = datetime.now().isoformat()
        #Adding the user to the right cognito group
        cognito.admin_add_user_to_group(UserPoolId=userPoolId, Username=username, GroupName='athletes')

        #Adding the user to the dynamodb table
        #Just making sure if we get a double invocation for whatever reason..
        print(f"Adding user to dynamo table {tableName}")
        table = dynamodb.Table(tableName)
        try: 
            item = table.query(
                KeyConditionExpression=boto3.dynamodb.conditions.Key('Userid').eq(userid)
            )['Items']
            if(item):
                print ("User already exists")
            else:
                try:
                    table.put_item(
                        Item={
                            'Userid': userid,
                            'Timestamp': date,
                            'Username': username,
                            'Email': email,
                            'Name': name,
                            'Preferred_username': preferred_username,
                            'Gender': gender,
                            'Weight': weight
                        }
                    )
                except Exception as e:
                    print(f"Error while adding user: {e}")
                    event['response'] = 'Failed to insert user into dynamo'
        except Exception as e:
            print(f"Error while fetching user: {e}")
            event['response'] = 'Failed to query dynamo while making sure there are no duplicates'
    except Exception as e:
        print (f"Error {e}")
        event['response'] = f"Something else happened {e}"
    return event