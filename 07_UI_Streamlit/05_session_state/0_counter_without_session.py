import streamlit as st

print('clicked')
st.title('Counter Example')
count = 0

increment = st.button('increment')

if(increment):
    count += 1

st.write(f'Count: {count}')