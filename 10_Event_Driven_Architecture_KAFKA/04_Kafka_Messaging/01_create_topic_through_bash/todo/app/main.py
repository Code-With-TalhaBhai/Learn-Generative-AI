from fastapi import FastAPI
from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app:FastAPI):
    print('string')



app = FastAPI(lifespan=lifespan)



@app.get('/')
def index():

    return {"Hello":"World"}