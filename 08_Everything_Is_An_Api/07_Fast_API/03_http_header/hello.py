from fastapi import FastAPI,Header
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'msg':'hello'}


# NOt working yet
@app.post('/hi')
def first(who=Header()):
    return {'msg':f'Hello, {who}'}



if __name__ == "__main__":
    uvicorn.run('hello:app',reload=True)