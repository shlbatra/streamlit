import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

#Title
st.title("Streamlit charts demo")

#Generate sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['A','B','C']
)

# Area chart section
st.subheader("Area chart")
st.area_chart(chart_data)

# Bar chart section
st.subheader("Bar chart")
st.bar_chart(chart_data)

# Line chart section
st.subheader("Line chart")
st.line_chart(chart_data)

# Scatter chart
st.subheader("Scatter chart")
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.scatter_chart(scatter_data)

# Display random points on a map
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat','lon']
)

#Pyplot section
st.subheader("Pyplot chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)