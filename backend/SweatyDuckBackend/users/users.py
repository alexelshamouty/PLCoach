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
        username = userAttributes['username']
        email = userAttributes['email']
        name = userAttributes['name']
        preferred_username = userAttributes['preferred_username']
        gender = userAttributes['gender']
        weight = userAttributes.get('custom:weight', '0')
        date = datetime.datetime.now().isoformat()
        #Adding the user to the right cognito group
        cognito.group_add_user(UserPoolId=userPoolId, Username=username, Groupname='athletes')

        #Adding the user to the dynamodb table
        #Just making sure if we get a double invocation for whatever reason..
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
                    print("Error while inserting user: " + e)
                    event['response'] = 'Failed to insert user into dynamo'
        except Exception as e:
            print("Error while fetching user: " + e)
            event['response'] = 'Failed to query dynamo while making sure there are no duplicates'
    except Exception as e:
        print ("Error " + e)
        event['response'] = f"Something else happened {e}"
    return event