import streamlit as st


prompt =  st.chat_input('Ask Something?')

if 'data' not in st.session_state:
    st.session_state.data = []

if(prompt):
    st.session_state.data.append(prompt)
    st.write(f'User has send the following message: {prompt}')


st.write(st.session_state.data)