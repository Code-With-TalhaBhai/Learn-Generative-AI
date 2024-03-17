import streamlit as st
import time


with st.status('Authenticaing...',expanded=True) as s:
    st.write('Please wait...')
    time.sleep(2)
    s.update(label="You are logged in",expanded=False)