import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

#Title
st.title("Streamlit forms demo")

# Form to hold the interactive elements
with st.form(key = "sample_form"):
    #Text input
    st.subheader("Text inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")

    # Date and time inputs
    st.subheader("Date & Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")

    #Selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["option1", "option2","option3"])
    gender = st.selectbox("Select gender", ["male","female","other"])
    slider_value = st.select_slider("Select range", options=[1,2,3,4,5])

    # Toggles and checkboxes
    st.subheader("Toggles and Checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toggle_value = st.checkbox("Enable darkmode?", value=False)

    #Submit button for form
    submit_button = st.form_submit_button(label="Submit")

# Outside of form
st.subheader("Buttons")
if st.button("Click me"):
    st.write(f"Hello, {name}!")
    

