import streamlit as st
from model import OpenAIBot
import time

# For webpage icons
st.set_page_config(page_title="Technology Tutor", page_icon=":speech_balloon:")


st.title('IT Expert')
st.write('Tutor will help you answer your questions about IT')


if "bot" not in st.session_state:
    st.session_state['bot'] = OpenAIBot(name='MyITBot',
    instructions="You are a technology bot. Answer questions about trending technologies")


for msg in st.session_state['bot'].get_messages():
    with st.chat_message(msg.role):
        st.markdown(msg.content)


prompt = st.chat_input('Your questions about IT?')

if prompt:
    with st.chat_message('user'):
        st.markdown(prompt)


    st.session_state['bot'].send_message(prompt)
    with st.spinner('Generating your answer'):
        time.sleep(5)

    if(st.session_state['bot'].isRunCompleted()):
        answer = st.session_state['bot'].get_latest_response()
        with st.chat_message(answer.role):
            st.markdown(answer.content)


# st.session_state['bot'].
