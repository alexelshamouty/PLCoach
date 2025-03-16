from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from utils.response_utils import ResponseUtils
from utils.db_utils import DBUtils
import logging 
from typing import List
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
            
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

userTable = os.environ['TABLE_NAME']
templateTableName = os.environ['TEMPLATE_TABLE_NAME']

@app.post("/createTracker")
def create_tracker(newTracker: dict):
    templateTable = DBUtils(templateTableName)
    response = templateTable.save_template(newTracker)
    if response:
        logger.error(f"Error saving template: {response}")
        raise HTTPException(status_code=500, detail=response)
    logger.info(f"New template is saved {newTracker}")
    return {"It went well": "itWentWell"}

def handler(event, context):
    # Handle warmup event
    if event.get("source") == "serverless-plugin-warmup":
        logger.info("Event received: %s", event)
        return {}
    try:
        responseUtils = ResponseUtils(logger)
        logger.info(f"Starting ASGI handler {event}")
        asgi_handler = Mangum(app)
        response = asgi_handler(event, context)
    except Exception as e:
        logger.error("Error processing request: %s", str(e))
        response = responseUtils.error_response(500, message=str(e))
    return response