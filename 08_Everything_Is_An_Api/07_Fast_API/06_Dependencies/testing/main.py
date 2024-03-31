from fastapi import FastAPI,HTTPException,status,Depends 
from typing import Annotated
import uvicorn


development_db = ["DB for Development"]


def get_db_session():
    return development_db


app = FastAPI()

@app.get('/')
def home():
    return {"home":"working"}

@app.get('/add-item')
def add_item(item:str,db:Annotated[list[str],Depends(get_db_session)]):
# def add_item():
    db.append(item)
    print(db)
    # return {"message":f"added item {item}"}
    return {"message":f"added item {db[-1]}"}


if __name__ == "__main__":
    uvicorn.run('main:app',reload=True)