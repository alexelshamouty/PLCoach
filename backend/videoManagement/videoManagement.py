import boto3.session
from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException
from fastapi import Depends
from fastapi import status
from fastapi import UploadFile
from fastapi import File
from typing import Optional

from utils.db_utils import DBUtils
from utils.response_utils import ResponseUtils
from handlers import (
    get_user_videos_handler,
    get_coach_videos_handler,
    upload_video_handler,
    update_coach_video_handler,
    update_user_video_handler,
    delete_coach_video_handler,
    delete_user_video_handler,
)

from generate_pre_signed_post_handler import generate_pre_signed_post_handler

import os 
import logging

import boto3 

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_TABLE = os.environ.get("VIDEO_TABLE","videoTable")
BUCKET_NAME = os.environ.get("VIDEO_BUCKET","sweatyducksco")
videoTable = DBUtils(USER_TABLE)


# GET endpoints
@app.get("/getUserVideos")
async def get_user_videos(userID: str):
    """
    Get videos uploaded by the user
    """
    return get_user_videos_handler(videoTable, userID)


@app.get("/getCoachVideos")
async def get_coach_videos(userID: str):
    """
    Get videos uploaded by coaches
    """
    return get_coach_videos_handler(videoTable, userID)


@app.post("/uploadUserVideo")
async def generate_pre_signed_post(userID: str, filename: str, exercise_path: str, comment: str):
    """
    Generate a pre-signed POST URL for uploading a video directly to S3
    
    Parameters:
    - userID: The ID of the user requesting upload access
    - filename: Name of the file to be uploaded
    - expiration: URL expiration time in seconds (default: 1 hour)
    """
    session = boto3.session.Session(profile_name='wetbox')
    s3_client = session.client('s3')
    return generate_pre_signed_post_handler(s3_client, BUCKET_NAME, videoTable, userID, filename, exercise_path, comment)

@app.post("/uploadCoachVideo")
async def generate_pre_signed_post_coach(userID: str, filename: str, exercise_path: str, comment: str):
    """
    Generate a pre-signed POST URL for uploading a coach video directly to S3
    
    Parameters:
    - userID: The ID of the user requesting upload access
    - filename: Name of the file to be uploaded
    - expiration: URL expiration time in seconds (default: 1 hour)
    """
    session = boto3.session.Session(profile_name='wetbox')
    s3_client = session.client('s3')
    return generate_pre_signed_post_handler(s3_client, BUCKET_NAME, videoTable, userID, filename, exercise_path, coach=True)

# PUT endpoint
@app.put("/uploadVideo")
async def upload_video(
    file: UploadFile = File(...),
    title: str = None,
    description: Optional[str] = None,
    type: str = None,
    dayId: str = None,
    exerciseName: str = None,
    exerciseLabel: str = None,
    block: str = None,
    week: str = None
):
    """
    Upload a new video (coach or athlete)
    """
    return upload_video_handler(
        videoTable,
        file,
        title,
        description,
        type,
        dayId,
        exerciseName,
        exerciseLabel,
        block,
        week
    )


# POST endpoints
@app.post("/updateCoachVideo")
async def update_coach_video(videoID: str):
    """
    Update an existing coach video
    """
    return update_coach_video_handler(videoTable, videoID)


@app.post("/updateUserVideo")
async def update_user_video(videoID: str, userID: str):
    """
    Update an existing user video
    """
    return update_user_video_handler(videoTable, videoID, userID)


# DELETE endpoints
@app.delete("/deleteCoachVideo")
async def delete_coach_video(video_id: str):
    """
    Delete a coach video by ID
    """
    return delete_coach_video_handler(videoTable, video_id)


@app.delete("/deleteUserVideo")
async def delete_user_video(video_id: str, userID: str):
    """
    Delete a user video by ID
    """
    return delete_user_video_handler(videoTable, video_id, userID)


def handler(event, context):
    if event.get("source") == "serverless-plugin-warmup":
        logger.info("Warming up event received: %s", event)
        return {}
    try:
        logger.info(f"Starting ASGI handler {event}")
        #TODO ( Authentication and Authorization)
        # Needs to be done here before passing to Mangum and any handler
        asgi_handler = Mangum(app)
        response = asgi_handler(event, context)
    except Exception as e:
        logger.error("Error processing request: %s", str(e))
        response = JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(e)},
        )
    return response
