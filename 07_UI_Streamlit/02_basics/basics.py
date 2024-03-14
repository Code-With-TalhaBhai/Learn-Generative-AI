import streamlit as st

st.success("My success");
st.info("This is information")
st.error("This is really error")
st.warning("This is last warning")
st.exception(ZeroDivisionError("This is zero division error"))


from PIL import Image
img = Image.open('../focused.webp')


st.image(img,width=230)

#  CheckBox
status = st.checkbox("I agree")
if(status):
    st.text("You are agreed")
else:
    st.text("Plz! tell us your choice")


# Radio
program = st.radio("Choose one",['DSA','AI'])
if program == 'DSA':
    st.warning(program) 
else:
    st.info(program)


about = st.button('Click Me')
if(about):
    st.write("You just clicked me");



# Text Input
name = st.text_input("First name")
if(st.button('Submit')):
    st.success("My name is "+name.title())



selected_value = st.slider("Give Your range",1,10)
st.text(f'selected_value: {selected_value}')