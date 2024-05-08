import os
from dotenv import find_dotenv,load_dotenv
from sqlmodel import SQLModel,create_engine,Field


### Engine() is used to create migrations i.e create tables only it can perform only raw sql queries


load_dotenv(find_dotenv())
database_url = os.environ.get('DATABASE_URL')



class Hero(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    name: str
    # name: str = Field(index=True) To define index for fast queries
    secret_name: str
    age: int | None = None



engine = create_engine(database_url,echo=True)

def create_table():
    SQLModel.metadata.create_all(engine) # Creating migration (table+schema)


if __name__ == "__main__":
    create_table()