import streamlit as st

st.title("Counter example with immediate rerun")

if "counter" not in st.session_state:
    st.session_state.counter = 0

def inc_and_rerun():
    st.session_state.counter += 1
    st.rerun()

st.write(f"Counter value: {st.session_state.counter}") 

if st.button("Inc and update immediately"):
    inc_and_rerun()