import streamlit as st


st.title("Counter Examples Using Callbacks")

if 'count' not in st.session_state:
    st.session_state.count = 0



def increment_counter(value):
    st.session_state.count += value


increment = st.number_input("Enter how much you increment",value=1,step=1)
increment_button = st.button('Increment',on_click=increment_counter,args=(increment,)) 

st.title(f'Total count is: {st.session_state.count}')

