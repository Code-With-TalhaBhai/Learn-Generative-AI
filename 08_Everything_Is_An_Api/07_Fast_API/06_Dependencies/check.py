from fastapi import FastAPI
from typing import List
import time

app : FastAPI = FastAPI()

@app.get('/')
def index():
    return{"msg":"world"}


def my():
    time.sleep(3)
    return "myself is very good"

@app.get('/check')
def check(sell:my):
    return {"yourself":sell}


if __name__ in "__main__":
    import uvicorn
    uvicorn.run("check:app",reload=True)