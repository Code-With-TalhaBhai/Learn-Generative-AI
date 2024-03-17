import streamlit as st
import time


st.subheader('This is before empty')

with st.empty():
    for seconds in range(10):
        st.write(f'{seconds} seconds')
        time.sleep(1)
    st.write('10 seconds over')


st.subheader('This is after empty')