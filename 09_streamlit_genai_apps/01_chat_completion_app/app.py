import streamlit as st
from model import MyBotModel

role = ['user','assistant']

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

if "bot" not in st.session_state:
    print('not in session')
    st.session_state.bot = MyBotModel('AI_BOT')


# chat_message = [{role:'user'|'assistant',content:'some string'}]

# Display Chat messages
for message in st.session_state['bot'].get_messages():
    avatar = BOT_AVATAR if message['role'] == 'assistant' else USER_AVATAR
    with st.chat_message(name=message['role'],avatar=avatar):
        st.markdown(message['content'])

with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state['bot'].delete_chat_history()



# Main ChatGPT Interface
prompt = st.chat_input('What do you want to ask?')
if(prompt):
    with st.chat_message("user",avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("ChatGPT",avatar=BOT_AVATAR):
        msg_placeholder = ""
        prompt_to_send = {"role":"user","content":prompt}

        stream = st.session_state['bot'].send_message(prompt_to_send)

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                msg_placeholder += chunk.choices[0].delta.content

        st.markdown(msg_placeholder)
        full_message = {"role":"assistant","content":msg_placeholder}
        st.session_state['bot'].append_message(full_message)

st.session_state['bot'].save_chat_history()



