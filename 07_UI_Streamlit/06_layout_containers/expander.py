import streamlit as st


expand = st.expander('My Custom Expander')


with expand:
    st.header("This is heading of expander")
    st.image('../focused.webp')
    st.text('This is footer of expander')