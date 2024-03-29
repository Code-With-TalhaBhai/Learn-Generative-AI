from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def spec():
    return {"msg": "Hello world"}


@app.get('/profile')
def index(filter:str):
    return {"profile":filter}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("filter:app",reload=True)