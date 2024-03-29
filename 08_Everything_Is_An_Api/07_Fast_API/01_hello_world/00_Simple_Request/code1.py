from fastapi import FastAPI

app : FastAPI = FastAPI()


@app.get('/')
def index():
    return {"msg":"hello world"}


# To get rid of starting server from cmd
if __name__ == "__main__": # First time run `name`s value is "__main__"
    import uvicorn
    uvicorn.run(app="code1:app",reload=True)