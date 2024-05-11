import os
from dotenv import find_dotenv,load_dotenv
from sqlmodel import create_engine


load_dotenv(find_dotenv())
database_url = os.environ.get('DATABASE_URL')
print('databased_url: ',database_url)


engine = create_engine(database_url,echo=True)
