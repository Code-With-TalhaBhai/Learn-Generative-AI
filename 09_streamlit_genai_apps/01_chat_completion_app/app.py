import streamlit as st

role = ['user','assistant']


with st.chat_message('ChatGPT'):
    st.markdown('This is my first message')

st.chat_message('Talha')
st.markdown('This is my first message')


st.chat_input('Say Something')
