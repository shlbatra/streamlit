import streamlit as st

st.write("Hello World") # Magic command write anything you give it

st.write({"key": "value"})

3+4 # automatically write as well

# Streamlit dataflow - any change streamlit run entire file

pressed = st.button("Press me") # by default false until press when it changes to true - rerun entire python code
print(pressed)

pressed2 = st.button("Press me second button")
print(pressed2)