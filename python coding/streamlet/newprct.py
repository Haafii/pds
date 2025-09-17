import streamlit as st
from pyecharts.charts import Line, Scatter, Bar, Pie
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

# Sample data (replace this with actual windy.com data)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
wind_speeds = [12, 17, 14, 19, 16]
temperatures = [28, 30, 27, 29, 31]
conditions = ["Clear", "Rainy", "Clear", "Cloudy", "Rainy"]

st.title("Windy.com Weather Data Visualizations")

# Line Chart: Daily wind trend
line = (
    Line()
    .add_xaxis(days)
    .add_yaxis("Wind Speed", wind_speeds)
    .set_global_opts(title_opts=opts.TitleOpts(title="Daily Wind Trend"))
)
st.subheader("Line Chart: Daily Wind Trend")
st_pyecharts(line)

# Scatter Plot: Specific day comparison (temperatures per day)
scatter = (
    Scatter()
    .add_xaxis(days)
    .add_yaxis("Temperature", temperatures)
    .set_global_opts(title_opts=opts.TitleOpts(title="Specific Day Comparison"))
)
st.subheader("Scatter Plot: Specific Day Comparison")
st_pyecharts(scatter)

# Bar Chart: Daily temperatures
bar = (
    Bar()
    .add_xaxis(days)
    .add_yaxis("Temperature", temperatures)
    .set_global_opts(title_opts=opts.TitleOpts(title="Daily Temperatures"))
)
st.subheader("Bar Chart: Daily Temperatures")
st_pyecharts(bar)

# Pie Chart: Each day's condition for 5 days
# Count occurrences of each condition
from collections import Counter
condition_counts = Counter(conditions)
pie_data = [(cond, count) for cond, count in condition_counts.items()]

pie = (
    Pie()
    .add("", pie_data)
    .set_global_opts(title_opts=opts.TitleOpts(title="Day Condition Distribution for 5 Days"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
st.subheader("Pie Chart: Day Condition Distribution")
st_pyecharts(pie)