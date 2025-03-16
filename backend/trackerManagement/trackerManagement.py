from fastapi import FastAPI, HTTPException, Request
from mangum import Mangum
from utils.response_utils import ResponseUtils
from utils.db_utils import DBUtils
import logging 
from typing import List
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    aws_event = request.scope.get("aws.event")
    aws_event_source = aws_event.get("source")
    if(aws_event_source == "serverless-plugin-warmup"):
        logger.info("WarmUp event received")
        return {}
    
@app.post("/createTrackerTemplate")
def read_trackerManagment(newTracker: List):
    logging.info("Request received {newTracker}")
    return {"It went well": "itWentWell"}

handler = Mangum(app)