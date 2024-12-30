import streamlit as st
import pandas as pd
import numpy as np

def intro():
    st.title("Welcome to app")
    st.write("This is intro page. Use dropdown to navigate to diff demos")

def plotting_demo():
    st.title("Plotting demo")
    st.write("Here we create simple plot")
    chart_data = pd.DataFrame(np.random.randn(50,3), columns=["a","b","c"])
    st.line_chart(chart_data)

def mapping_demo():
    st.title("Mapping demo")
    st.write("This page shows map with random points")

    map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat","lon"])
    st.map(map_data)


def data_frame_demo():
    st.title("Dataframe demo")
    st.write("Here we display sample dataframe")

    df = pd.DataFrame(
        np.random.randn(20,3),
        columns = ["col1","col2","col3"]
    )

    st.dataframe(df)

page_names_to_funcs = {
    "-": intro,
    "Plotting demo": plotting_demo,
    "Mapping demo": mapping_demo,
    "Dataframe demo": data_frame_demo
}

selected_page = st.sidebar.selectbox("Choose page", options=page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

