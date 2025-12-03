

import streamlit as st

weight = st.number_input("Enter your weight in kg:")   
height = st.number_input("Enter your height in meters:")

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write("Your BMI is: ", bmi)


















