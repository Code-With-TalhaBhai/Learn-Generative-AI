import streamlit as st


# Everything is available in st.secrets dict:
st.write(f'My DB name is: {st.secrets["db_username"]}')
st.write(f'My DB password is: {st.secrets["db_password"]}')


