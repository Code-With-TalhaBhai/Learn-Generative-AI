import streamlit as st


tab1, tab2, tab3 = st.tabs(["My Tab 1", "My Tab2","My tab3"])

with tab1:
    st.header('This is header 1')
    st.image('../focused.webp')


with tab2:
    st.header('This is header 2')
    st.image('https://i.ytimg.com/vi/339amTioakE/hqdefault.jpg')


with tab3:
    st.header('This is header 1')
    st.image('../focused.webp')