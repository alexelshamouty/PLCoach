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
    finalize_upload_handler
)

from generate_pre_signed_post_handler import generate_pre_signed_post_handler

import os 
import logging

import boto3 
from botocore.config import Config

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
BLOCK_TABLE = os.environ.get("BLOCK_TABLE","blocks-dev")
BUCKET_NAME = os.environ.get("VIDEO_BUCKET","sweatyducksco-dev")
videoTable = DBUtils(USER_TABLE)


# GET endpoints
@app.get("/getVideos")
async def get_user_videos(userID: str, blockName: str, week: str, dayId: str, exerciseName: str):
    """
    Get videos uploaded by the user
    """
    logger.info("Fetching videos for user %s", userID)
    blockTable = DBUtils(BLOCK_TABLE)
    # Fetch the block
    block, error = blockTable.get_block_by_name(userID, blockName)
    if error:
        logger.error("Error retrieving block: %s", error)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Block not found",
    )

    week_data = block.get("Block", {}).get("Weeks", {}).get(week)
    if not week_data:
        logger.error("Week %s not found in block %s", week, block)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Week not found",
        )

    # Access the day
    day_data = week_data.get("Days", {}).get(dayId)
    if not day_data:
        logger.error("Day %s not found in week %s", dayId, week)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Day not found",
        )
    
    exercises = day_data.get("Exercises", [])

    excersise = next((ex for ex in exercises if ex.get("name") == exerciseName), None)

    if not excersise:
        logger.error("Exercise %s not found in day %s", exerciseName, dayId)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercise not found",
        )
    
    videos = excersise.get("Videos", [])
    if not videos:
        logger.error("No videos found for exercise %s", exerciseName)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No videos found",
        )
    logger.info(f"Videos found for user {videos}")
    return videos


@app.post("/uploadVideo")
async def generate_pre_signed_post(userID: str, filename: str, title:str, exercise_path: str, contentType:str, comment: str):
    """
    Generate a pre-signed POST URL for uploading a video directly to S3
    
    Parameters:
    - userID: The ID of the user requesting upload access
    - filename: Name of the file to be uploaded
    - expiration: URL expiration time in seconds (default: 1 hour)
    """
    #TODO We need somethng here to route between admin and non admin..
    logger.info("Generating pre-signed URL for user %s", userID)
    #This is so annoying...
    session = boto3.session.Session()
    s3_client = session.client('s3',config=Config(signature_version='s3v4'))
    return generate_pre_signed_post_handler(s3_client, BUCKET_NAME, videoTable, userID, filename, exercise_path, title, contentType, comment)

@app.post("/finalizeUpload")
def finalize_upload(
    s3Key: str,
    title: str,
    filetype: str,
    description: str,
    dayId: str,
    exerciseName: str,
    exerciseLabel: str,
    block: str,
    week: str,
    userID: str,
    # Optional parameters
    type: Optional[str] = "athlete",
):
    """
    Finalize the upload process by extracting metadata and updating the block table.
    """
    return finalize_upload_handler(
        s3Key, title, filetype, description, dayId, exerciseName, exerciseLabel, block, week, userID, type
    )

@app.post("/updateVideo")
async def update_video():
    """
    Update a video by ID
    """
    return {}


@app.delete("/deleteVideo")
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
