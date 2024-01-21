import datetime
from fastapi import FastAPI

from app.graphql.main import graphql_app

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/ping")
def serverInfo():
    return {
        "time": datetime.datetime.now(),
        "info": {"name": "strawberry", "python": "3.9", "fastapi": "1.109"},
    }


app.include_router(graphql_app, prefix="/graphql")
