from fastapi import FastAPI

import datetime

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
