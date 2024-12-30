import streamlit as st

# widgets hold state ex. buttons , used in forms

st.button("Ok") # each element assigned key or id 
st.button("Ok", key="btn2")

min_value = st.slider("set min value", 0, 50, 25) # min, max, defaukt
slider_value = st.slider("set slider value", min_value, 100, min_value) # new id assigned everytime min_value is changed

if "slider" not in st.session_state:
    st.session_state.slider = 25

st.session_state.slider = st.slider("slider", min_value, 100, st.session_state.slider)

# If widget not rendered on screen then its state is destroyed - need to cache it

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show input field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something: ", value = st.session_state.user_input) # to keep state as not rendered - , value = st.session_state.user_input
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input","")

st.write(f"User Input: {user_input}")