from fastapi import FastAPI, HTTPException
from magnum import Magnum

app = FastAPI()

handler = Magnum(app)