import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime

#Title
st.title("User Information Form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

with st.form(key="user_info_form"): # only update when hit submit button in form
    form_values["name"] = st.text_input("Enter your name")
    form_values["height"] = st.number_input("Enter your height in cm")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"]) 
    form_values["dob"] = st.date_input("Enter your birth date", max_value = max_date, min_value = min_date)

    if form_values["dob"]: # use session state for dyanmic updating outside form
        age = max_date.year - form_values["dob"].year
        if form_values["dob"].month > max_date.month or (form_values["dob"].month  == max_date.month and form_values["dob"].day > max_date.day):
            age -= 1
        st.write(f"Your calculated age is {age} years")
    
    submit_button = st.form_submit_button(label = "Submit")
    if submit_button: # Nest logic inside form, can be done outside form as well by moving this outside with
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
            st.write(f"Your age is {age}")