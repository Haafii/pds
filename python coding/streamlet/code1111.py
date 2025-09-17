import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="📊 Sales Dashboard - Pro", layout="wide")

# -------------------------
# Custom CSS with Images
# -------------------------
st.markdown("""
    <style>
    .kpi-box {
        background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                    url('https://www.transparenttextures.com/patterns/cubes.png');
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-weight: 600;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
        height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background-size: cover;
    }
    .kpi-title {
        font-size: 18px;
        color: #2c3e50;
    }
    .kpi-value {
        font-size: 22px;
        font-weight: bold;
        color: #34495e;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Dummy Data
# -------------------------
np.random.seed(20)
dates = pd.date_range("2023-01-01", "2023-12-31")
data = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(1500, 7000, len(dates)),
    "Profit": np.random.randint(400, 1500, len(dates)),
    "Quantity": np.random.randint(1, 70, len(dates)),
    "Category": np.random.choice(["Furniture", "Technology", "Office Supplies"], len(dates)),
    "Segment": np.random.choice(["Consumer", "Corporate", "Home Office"], len(dates)),
    "Region": np.random.choice(["East", "West", "Central", "South"], len(dates))
})

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("🎯 Filters")
seg = st.sidebar.multiselect("Choose Segment", options=data["Segment"].unique(), default=data["Segment"].unique())
cat = st.sidebar.multiselect("Choose Category", options=data["Category"].unique(), default=data["Category"].unique())
df = data[(data["Segment"].isin(seg)) & (data["Category"].isin(cat))]

# -------------------------
# KPIs Row with Images
# -------------------------
st.title("📊 Sales Dashboard - Pro Version")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.markdown(f"<div class='kpi-box'><span class='kpi-title'>💰 Revenue</span><span class='kpi-value'>${df['Sales'].sum():,}</span></div>", unsafe_allow_html=True)
kpi2.markdown(f"<div class='kpi-box'><span class='kpi-title'>📦 Orders</span><span class='kpi-value'>{len(df):,}</span></div>", unsafe_allow_html=True)
kpi3.markdown(f"<div class='kpi-box'><span class='kpi-title'>📈 Profit %</span><span class='kpi-value'>{round((df['Profit'].sum()/df['Sales'].sum())*100, 2)}%</span></div>", unsafe_allow_html=True)
kpi4.markdown(f"<div class='kpi-box'><span class='kpi-title'>🛒 Quantity</span><span class='kpi-value'>{df['Quantity'].sum():,}</span></div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# Charts (New Color Palette)
# -------------------------
row1 = st.columns([1, 1])
with row1[0]:
    fig = px.pie(df, names="Segment", values="Sales", title="Sales by Segment",
                 color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig, use_container_width=True)

with row1[1]:
    fig = px.treemap(df, path=["Segment", "Category"], values="Sales",
                     title="Segment-Category Breakdown", color_discrete_sequence=px.colors.sequential.Purples)
    st.plotly_chart(fig, use_container_width=True)

row2 = st.columns([2, 1])
with row2[0]:
    fig = px.line(df, x="Date", y="Sales", title="Revenue Trend", markers=True,
                  line_shape="spline", color_discrete_sequence=["#2980b9"])
    st.plotly_chart(fig, use_container_width=True)

with row2[1]:
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()
    fig = px.bar(region_sales, x="Region", y="Sales", text_auto=True,
                 title="Revenue by Region", color_discrete_sequence=["#8e44ad"])
    st.plotly_chart(fig, use_container_width=True)
