from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from sqlmodel_api.models import Todo
from sqlmodel_api.connect import engine


def create_tables():
    SQLModel.metadata.create_all(engine)
    print(Todo)

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    print('table has created')
    yield
    # print('life span end')



app = FastAPI(title="FastAPI_SQLMODEL_TODO",lifespan=lifespan)



@app.get('/')
def showItems():
    return {"show":"home is good"}


@app.get('/create-item')
def addItem():
    return "Item is added with id"


@app.get('/update-item')
def updateItem():
    return "Update item with id"

@app.get('/delete-item')
def deleteItem():
    return "Deleted Items"

