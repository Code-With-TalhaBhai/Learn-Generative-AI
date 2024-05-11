from dotenv import find_dotenv,load_dotenv
import os
from sqlmodel import create_engine


find_dotenv(load_dotenv())
database_url = os.environ.get('DATABASE_URL')
print('databased_url: ',database_url)


engine = create_engine(database_url,echo=True)
