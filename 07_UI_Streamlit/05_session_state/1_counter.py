import streamlit as st


st.write(st.session_state)

if "count" not in st.session_state:
    st.session_state.count = 0


increment = st.button('increment')

if(increment):
    st.session_state.count += 1


st.write(f'Count: {st.session_state.count}')