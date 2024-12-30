import streamlit as st
import time

# Cache data ex for API calls for every user for every session - central webserver to utilize cache for every user, cache is global
# Use for immutable data even if modified from external source

@st.cache_data(ttl=60) #cache this data for 60 sec
def fetch_data():
    # simulate slow data fetching process
    time.sleep(10)
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)


# Cache resource - return reference to resource

file_path = "example.txt" 

@st.cache_resource # get mutable copy here - every user share the same file
def get_file_handler():
    # open file in append mode that creates the file if not exist
    file = open(file_path, "a+")
    return file

# use cached file handler
file_handler = get_file_handler()

# write to file using cached file handler

if st.button("Write to file"):
    file_handler.write("New line of text\n")
    file_handler.flush() # ensure content written immediately
    st.success("Wrote new line to file!")

if st.button("Read file"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)

# Always close file when done
st.button("Close file", on_click=file_handler.close)