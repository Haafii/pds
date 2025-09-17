import streamlit as st
import pandas as pd
from pyecharts.charts import Line, Bar, Scatter, Pie
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

st.set_page_config(page_title="Vellore Weather Dashboard", layout="wide")
st.title("Vellore Weather Dashboard (Last 5 Days)")

# ---------------- Load Dataset ----------------
@st.cache_data
def load_data():
    df = pd.read_excel("vellore_last_5_days_hourly_weather.xlsx", sheet_name="Sheet1")
    # Create datetime column from date + time
    df["datetime"] = pd.to_datetime(df["date"].astype(str) + " " + df["time"].astype(str))
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

df = load_data()

# ---------------- Sidebar Options ----------------
chart_type = st.sidebar.radio(
    "Choose a Visualization",
    ["Line Chart - Daily Wind Trend",
     "Bar Chart - Daily Temperatures",
     "Scatter Plot - Temp vs Wind (All Days)",
     "Pie Chart - Wind Contribution"]
)

# ---------------- Chart Functions ----------------
def line_daily_wind(df):
    daily_wind = df.groupby("date")["wind_kph"].mean().reset_index()
    line = (
        Line()
        .add_xaxis(daily_wind["date"].astype(str).tolist())
        .add_yaxis("Avg Wind Speed (km/h)", daily_wind["wind_kph"].round(2).tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Daily Average Wind Speed"),
            xaxis_opts=opts.AxisOpts(name="Date"),
            yaxis_opts=opts.AxisOpts(name="Wind (km/h)")
        )
    )
    return line

def bar_daily_temp(df):
    daily_temp = df.groupby("date")["temp_c"].mean().reset_index()
    bar = (
        Bar()
        .add_xaxis(daily_temp["date"].astype(str).tolist())
        .add_yaxis("Avg Temp (°C)", daily_temp["temp_c"].round(1).tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Daily Average Temperatures"),
            xaxis_opts=opts.AxisOpts(name="Date"),
            yaxis_opts=opts.AxisOpts(name="Temperature (°C)")
        )
    )
    return bar

def scatter_temp_vs_wind(df):
    scatter = Scatter()
    for d in df["date"].unique():
        sub = df[df["date"] == d]
        scatter.add_xaxis(sub["temp_c"].round(1).tolist())
        scatter.add_yaxis(str(d), sub["wind_kph"].round(2).tolist(), symbol_size=10)
    scatter.set_global_opts(
        title_opts=opts.TitleOpts(title="Temperature vs Wind Speed (All Days)"),
        xaxis_opts=opts.AxisOpts(name="Temperature (°C)"),
        yaxis_opts=opts.AxisOpts(name="Wind Speed (km/h)"),
        tooltip_opts=opts.TooltipOpts(formatter="Temp: {c[0]}°C<br/>Wind: {c[1]} km/h")
    )
    return scatter

def pie_wind_contribution(df):
    daily_sum = df.groupby("date")["wind_kph"].sum().reset_index()
    data = [(str(d), round(v, 2)) for d, v in zip(daily_sum["date"], daily_sum["wind_kph"])]
    pie = (
        Pie()
        .add("", data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Wind Contribution by Day"),
            legend_opts=opts.LegendOpts(orient="horizontal", pos_bottom="0%")
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    )
    return pie

# ---------------- Render Selected Chart ----------------
if chart_type == "Line Chart - Daily Wind Trend":
    st_pyecharts(line_daily_wind(df))
elif chart_type == "Bar Chart - Daily Temperatures":
    st_pyecharts(bar_daily_temp(df))
elif chart_type == "Scatter Plot - Temp vs Wind (All Days)":
    st_pyecharts(scatter_temp_vs_wind(df))
elif chart_type == "Pie Chart - Wind Contribution":
    st_pyecharts(pie_wind_contribution(df))

# ---------------- Show Data ----------------
with st.expander("Show Raw Data"):
    st.dataframe(df.head(100), use_container_width=True)
