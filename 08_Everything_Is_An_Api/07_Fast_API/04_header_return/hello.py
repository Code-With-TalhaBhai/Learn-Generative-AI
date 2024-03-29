from fastapi import FastAPI,Header
import uvicorn


app = FastAPI()

@app.get('/')
def home():
    return {'msg':'hello'}

# NOt working yet
@app.post('/agent')
def index(user=Header()):
    return user



if __name__ == '__main__':
    uvicorn.run('hello:app',reload=True)