import streamlit as st


st.title("Counter Examples Using Callbacks")

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1


st.button('Increment 1',on_click=increment_counter)
st.button('Increment 2',on_click=increment_counter)
st.button('Increment 3',on_click=increment_counter)


st.title(f'total count is: {st.session_state.count}')