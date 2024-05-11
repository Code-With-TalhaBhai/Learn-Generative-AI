import os
from dotenv import find_dotenv,load_dotenv
from sqlmodel import create_engine
from sqlmodel import SQLModel,Field


load_dotenv(find_dotenv())
database_url = os.environ.get('DATABASE_URL')


engine = create_engine(database_url,echo=True)