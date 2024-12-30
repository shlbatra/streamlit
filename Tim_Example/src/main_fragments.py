import streamlit as st

# Fragments run separate ui components

st.title("My app explaining fragments")

@st.fragment() # run independently and not entire app when changed here, not return from fragments - use session state instead
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter Text")
    #st.rerun(scope="app") - rerun entire app , scope="fragment"

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("filter")
    new_cols[1].file_uploader("Upload image")
    new_cols[2].selectbox("Choose option", ["Option1","Option2","Option3"])
    new_cols[3].slider("select value", 0, 50, 100)
    new_cols[4].text_input("Enter text")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("select", [1,2,3],None) # affect entire app
cols[1].button("Update")
filter_and_file()