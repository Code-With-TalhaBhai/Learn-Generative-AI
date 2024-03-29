from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def index():
    return "hello world"


@app.get('/{name1}/pk/{name2}')
def names(name1:str,name2:str):
    return {"name1":name1,"name2":name2}


if __name__ in "__main__":
    import uvicorn
    uvicorn.run("arg:app",reload=True)
