import os
from dotenv import find_dotenv,load_dotenv
from sqlmodel import create_engine
from sqlmodel import SQLModel,Field


load_dotenv(find_dotenv())
database_url = os.environ.get('DATABASE_URL')


engine = create_engine(database_url,echo=True)



class Team(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    name : str = Field(index=True)
    headquarters : str


class Hero_T(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    name: str = Field(index=True)
    secret_name : str
    age : int | None 
    team_id : int | None = Field(default=None,foreign_key="team.id")


def create_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()