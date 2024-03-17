import streamlit as st


col1,col2,col3 = st.columns(3)

with col1:
    st.header('Col 1')
    st.image('./../focused.webp')

with col2:
    st.header('Col 2')
    st.image('./../focused.webp')

with col3:
    st.header('Col 3')
    st.image('./../focused.webp')

