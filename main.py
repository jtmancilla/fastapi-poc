import datetime

from fastapi import FastAPI
from pydantic import BaseModel


from helper import prepare_text
from helper import get_current_datetime

app = FastAPI()


class Item(BaseModel):
    data: str


@app.get("/")
async def index():
    return {
        "message": f"Hello from index {get_current_datetime()}"
    }


@app.get("/sentiment")
async def sentiment():
    return {
        "message": f"Hello from sentiment {get_current_datetime()}"
    }


@app.post("/sentiment")
async def sentiment(item: Item):
    return {
        "message": f"{prepare_text(item.data)} {get_current_datetime()}"
    }