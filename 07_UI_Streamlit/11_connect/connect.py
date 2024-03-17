import streamlit as st
from sqlalchemy import text


# connection url here
# conn = st.connection('soldier_db',type="sql",url="postgresql://postgres:admin@localhost:5432/postgres")


# connection details in secrets.toml file
# conn = st.connection('mypostgresdb',type='sql')

# connection url in secrets.tomal file
conn = st.connection('local',type='sql')

# with conn.session as s:
#     # s.execute(
#     #     text("insert into soldier (name,age,rank) values (:name,:age,:rank);")
#     #     ,params={'name':'Abrar','age':23,'rank':'Bergadier'})

#     s.execute(
#         text("insert into soldier (name,age,rank) values (:name,:age,:rank);")
#         ,{'name':'Mousa','age':22,'rank':'Core Commander'})
    
# #     s.execute(
# #         text('INSERT INTO soldier (name,age,rank) values (:name, :age, :rank);')
# #         ,params=dict(name='Khizer',age=23,rank='General'))
#     s.commit()


soldier_query = conn.query('select * from soldier',ttl=10) # ttl to remove caching of queries - this method 10s
df = st.dataframe(soldier_query)
print(soldier_query)