from fastapi import FastAPI
from model import Creature
from typing import List

app : FastAPI = FastAPI()

@app.get('/')
def index():
    return{"msg":"world"}


@app.get('/creatures')
def index()->List[Creature]:
    from data import get_creatures
    return get_creatures()



if __name__ in "__main__":
    import uvicorn
    uvicorn.run("web:app",reload=True)