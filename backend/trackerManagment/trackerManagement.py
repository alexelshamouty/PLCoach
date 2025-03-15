from fastapi import FastAPI, HTTPException, Request
from magnum import Magnum
from utils.response_utils import ResponseUtils
from utils.db_utils import DBUtils
import logging 

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

@app.get("/trackerManagement")
def read_trackerManagment():
    return {"Hello": "World"}

handler = Magnum(app)