import os
from dotenv import find_dotenv,load_dotenv
from sqlmodel import create_engine,Session,text


load_dotenv(find_dotenv())
database_url = os.environ.get('DATABASE_URL')

engine = create_engine(database_url,echo=True)

# if table_name is capitalize, then use quotations outside it, i.e "Course"
stmt1 = text('SELECT * FROM "Courses"')
stmt2 = text('SELECT * FROM "Programs"') 
stmt3 = text('SELECT * FROM playing_with_neon')
stmt4 = text('SELECT * FROM sample')


session = Session(engine)
result = session.exec(statement=stmt1)
for row in result:
    print(row)
session.close()


# print(engine)
# print(result)