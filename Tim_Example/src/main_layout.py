import streamlit as st

# Sidebar layout
st.sidebar.title("This is Sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text")
sidebar_input = st.sidebar.text_input("Enter something in sidebar")

tab1, tab2, tab3 = st.tabs(["Tab1","Tab2","Tab3"])

with tab1:
    st.write("You are in tab1")

with tab2:
    st.write("You are in tab2")

with tab3:
    st.write("You are in tab3")

# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("Col1")
    st.write("Content for Col1")
with col2:
    st.header("Col2")
    st.write("Content for Col2")

# Containers Example
with st.container(border=True):
    st.write("This is inside container")
    st.write("You can think of containers as grouping for elements")
    st.write("Containers help manage sections of page")

#Empty placeholder
placeholder = st.empty()
placeholder.write("This is empty placeholder, useful for dyanmic content")

if st.button("Update Placeholder"):
    placeholder.write("The content of placeholder has been updated")

# Expander
with st.expander("Expand for details"):
    st.write("This is additional info hidden by default")
    st.write("You can use expanders to keep your interface clean")

# Popover tooltip
st.write("Hover over button for tooltip")
st.button("Button with tooltip", help="This is tooltip or popover on hover")

# Sidebar input handling
if sidebar_input:
    st.write(f"You entered in sidebar: {sidebar_input}")