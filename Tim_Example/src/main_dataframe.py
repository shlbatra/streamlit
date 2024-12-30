import streamlit as st
import pandas as pd

st.title("Streamlit Elements Demo")

#Dataframe section
st.subheader("Dataframe")
df = pd.DataFrame({
    'Name': ['A','B','C','D'],
    'Age': [14, 98, 12, 33],
    'Occupation': ['Engineer','Doctor','Artist','Chef']
})
st.dataframe(df)

#Data Editor Section
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)

# Static Table
st.subheader("Static Table")
st.table(df)

# Metrics section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(), 1))

#JSON & Dict section
st.subheader("JSON & Dictionary")
sample_dict = {
    "name": "A",
    "age": 25,
    "skills": ["Python","DS","ML"]
}
st.json(sample_dict)

#Also show as dictionary
st.write("Dictionary View:", sample_dict)
