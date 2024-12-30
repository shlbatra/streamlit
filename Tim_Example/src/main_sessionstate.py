import streamlit as st

# Session state is something we can use to store values within the same user session, refresh web browser - session change - per user per web browser refresh

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter value: {st.session_state.counter}") 
