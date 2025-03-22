from fastapi.responses import JSONResponse
from fastapi import status
import os
import uuid
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def generate_pre_signed_post_handler(s3_client, bucket_name, video_table, user_id, filename, exercise_path, title, contentType, comment=None, coach=False):
    """
    Handler for generating pre-signed POST URLs for direct file uploads to S3
    
    Args:
        video_table: Database table for videos
        user_id: The ID of the requesting user
        filename: Name of the file to be uploaded
        expiration: URL expiration time in seconds (default: 1 hour)
        
    Returns:
        JSON response with pre-signed POST URL and required fields or error message
    """
    try:
        # Generate a unique key for the file
        file_extension = os.path.splitext(filename)[1]
        logger.info(f"File extension: {file_extension}")
        object_key = f"uploads/{user_id}/{str(uuid.uuid4())}{file_extension}"
        logger.info(f"Generated object key: {object_key}")
        logger.info(f"Parameters: {user_id}, {filename}, {exercise_path}, {comment}")
        logger.info({
                    'acl': 'private',
                    'x-amz-meta-exercise_path': exercise_path ,
                    'x-amz-meta-title': title,
                    'x-amz-meta-comment': comment if comment else '',
                })
        try:
            # Generate the presigned POST URL
            response = s3_client.generate_presigned_post(
                Bucket=bucket_name,
                Key=object_key,
                Fields={
                    'acl': 'private',
                    'x-amz-meta-exercise_path': exercise_path ,
                    'Content-Type': contentType,
                    'x-amz-meta-title': title,
                    'x-amz-meta-comment': comment if comment else '',
                },
                Conditions=[
                    {'acl': 'private'},
                    {'x-amz-meta-exercise_path': exercise_path},
                    {'Content-Type': contentType},
                    {'x-amz-meta-title': title},
                    {'x-amz-meta-comment': comment if comment else ''},
                ],
                ExpiresIn=300
            )
            
            # Return the pre-signed POST URL and fields
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "url": response['url'],
                    "fields": response['fields'],
                    "s3Key": object_key  # Return the key for later reference
                }
            )
            
        except ClientError as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"message": str(e)}
            )
            
    except Exception as e:
        logging.error(f"Error generating pre-signed POST URL: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(e)}
        )