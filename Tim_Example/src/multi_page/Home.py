import streamlit as st

st.title("Home")
st.text_input("Name")

if st.button("Home"):
    st.switch_page("Home.py")
if st.button("Page 1"):
    st.switch_page("pages/1_Page1.py")
if st.button("Page 2"):
    st.switch_page("pages/2_Page2.py")

# Investigate st.navigation from documentation