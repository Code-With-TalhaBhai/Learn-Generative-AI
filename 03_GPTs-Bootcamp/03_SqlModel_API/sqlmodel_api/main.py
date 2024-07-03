from fastapi import FastAPI,Body
from contextlib import asynccontextmanager
from sqlmodel import SQLModel,select,Session
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
    todos = []
    with Session(engine) as session:
        stmt = select(Todo)
        todos = session.exec(stmt).all()
    return todos


@app.get('/item/{id}')
def singleItem(id:int):
    todo = {}
    with Session(engine) as session:
        stmt = select(Todo).where(Todo.id == id)
        todo = session.exec(stmt).one()
    return todo


@app.post('/create-item')
def addItem(item=Body(embed=True)):
    print(item)
    todo = Todo(title=item['title'],description=item['description'])
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        print('simple id',todo.id)
    return todo


@app.get('/update-item/{id}')
def updateItem(id:int,newItem=Body(embed=True)):
    with Session(engine) as session:
        stmt = select(Todo).where(Todo.id == id)
        todo = session.exec(stmt).one()
        if newItem['title']:
            todo.title = newItem['title']
        if newItem['description']:
            todo.descriptio = newItem['description']
        if newItem['author']:
            todo.author = newItem['author']

        session.add(todo)
        session.commit()
        session.refresh(todo)
    return todo

@app.get('/delete-item/{id}')
def deleteItem(id:int):
    todo = {}
    with Session(engine) as session:
        stmt = select(Todo).where(Todo.id == id)
        todo = session.exec(stmt).one()
        session.delete(todo)
        session.commit()
    return todo

