from fastapi import FastAPI

app : FastAPI = FastAPI()


@app.get('/')
def index():
    return {"msg":"hello world"}