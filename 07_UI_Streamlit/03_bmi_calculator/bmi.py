# BODY MASS Index - BMI
import streamlit as st

st.header('Welcome To BMI Calculator')

weight = st.number_input("Enter your weight (in kgs)")

unit = st.radio("Select your height format: ",['cms','meters','feet'])

if(unit):
    height = st.number_input(unit)
    st.text("Enter some value of height")
    if(weight > 0 and height > 0):
        bmi = weight / ((height/3.28)**2)

calculate = st.button('Calcuate BMI')

if calculate:
    st.text(f'Your BMI Index is {bmi}')

    if(bmi<16):
        st.error("You are extremely underweight")
    elif(bmi>=16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi>=18.5 and bmi<25):
        st.success("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("Overweight")
    elif(bmi>=30):
        st.error("Extremely Overweight")





