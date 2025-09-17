import streamlit as st
from streamlit_echarts import st_echarts

st.title("📊 ECharts Visualizations in Python")

# Line Chart
st.subheader("Line Chart: Weekly Attendance")
line_options = {
    "xAxis": {"type": "category", "data": ["Mon", "Tue", "Wed", "Thu", "Fri"]},
    "yAxis": {"type": "value"},
    "series": [{"data": [80, 85, 78, 90, 88], "type": "line"}]
}
st_echarts(options=line_options)

# Bar Chart
st.subheader("Bar Chart: Subject Scores")
bar_options = {
    "xAxis": {"type": "category", "data": ["Math", "Physics", "Chemistry"]},
    "yAxis": {"type": "value"},
    "series": [{"data": [85, 90, 78], "type": "bar"}]
}
st_echarts(options=bar_options)

# Pie Chart
st.subheader("Pie Chart: Project Themes")
pie_options = {
    "series": [{
        "type": "pie",
        "data": [
            {"value": 40, "name": "AI"},
            {"value": 30, "name": "IoT"},
            {"value": 30, "name": "Healthcare"}
        ]
    }]
}
st_echarts(options=pie_options)

# Radar Chart
st.subheader("Radar Chart: Student Skills")
radar_options = {
    "radar": {
        "indicator": [
            {"name": "Coding", "max": 100},
            {"name": "Communication", "max": 100},
            {"name": "Teamwork", "max": 100}
        ]
    },
    "series": [{
        "type": "radar",
        "data": [{"value": [90, 70, 85], "name": "Student A"}]
    }]
}
st_echarts(options=radar_options)