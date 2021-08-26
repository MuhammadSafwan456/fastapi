import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    desc: Optional[str] = None


# simple route
@app.get("/")
def hello_world():
    return {"hello": "world"}


# path parameters
@app.get("/path_param/{_id}")
def path_param(_id: str):
    return {"id": _id}


# query param
@app.get("/query")
def query_param(city: str, country: str):
    return {"city": city, "country": country}


# request body with pydantic
@app.post('/item')
def items(item: Item):
    return item


# combo or all 3
@app.post('/item/{path_param}')
def items(item: Item, path_param: int, value: bool):
    return {"path_param": path_param,
            "body": item,
            "query_param": value}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
