import os
from dotenv import find_dotenv,load_dotenv
from sqlmodel import SQLModel,create_engine,Field


### Engine() is used to create migrations i.e create tables only it can perform only raw sql queries


load_dotenv(find_dotenv())
database_url = os.environ.get('DATABASE_URL')



class Hero(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    name: str
    secret_name: str
    age: int | None = None



engine = create_engine(database_url,echo=True)

def create_table():
    Hero(name="Talha",secret_name="tk")
    SQLModel.metadata.create_all(engine)


create_table()