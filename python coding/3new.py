import streamlit as st
from pyecharts.charts import Bar
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

# Define multiple datasets
data_options = {
    "Semester 1": ["Math", "Physics", "Chemistry"],
    "Semester 2": ["Biology", "English", "History"],
    "Semester 3": ["CS", "AI", "ML"]
}

value_options = {
    "Semester 1": [85, 90, 78],
    "Semester 2": [88, 76, 92],
    "Semester 3": [95, 89, 93]
}

# Sidebar selector
selected_semester = st.selectbox("Choose a semester", list(data_options.keys()))

# Get corresponding values
subjects = data_options[selected_semester]
scores = value_options[selected_semester]

# Create Bar chart
bar = (
    Bar()
    .add_xaxis(subjects)
    .add_yaxis("Scores", scores)
    .set_global_opts(title_opts=opts.TitleOpts(title=f"{selected_semester} Performance"))
)

# Display chart
st_pyecharts(bar)