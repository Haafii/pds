import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------
# Page Setup
# -------------------------
st.set_page_config(page_title="📊 Sales Dashboard", layout="wide")

# -------------------------
# Custom CSS for KPI Cards
# -------------------------
st.markdown("""
    <style>
    .kpi-card {
        background: #fdf2e9;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Dummy Data
# -------------------------
np.random.seed(42)
dates = pd.date_range("2023-01-01", "2023-12-31")
data = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(1000, 5000, len(dates)),
    "Profit": np.random.randint(200, 1000, len(dates)),
    "Quantity": np.random.randint(1, 50, len(dates)),
    "Category": np.random.choice(["Furniture", "Technology", "Office Supplies"], len(dates)),
    "Segment": np.random.choice(["Consumer", "Corporate", "Home Office"], len(dates)),
    "Region": np.random.choice(["East", "West", "Central", "South"], len(dates))
})

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("🔎 Filters")
seg = st.sidebar.multiselect("Segment", options=data["Segment"].unique(), default=data["Segment"].unique())
region = st.sidebar.multiselect("Region", options=data["Region"].unique(), default=data["Region"].unique())
df = data[(data["Segment"].isin(seg)) & (data["Region"].isin(region))]

# -------------------------
# KPIs
# -------------------------
st.title("📊 Sales Dashboard (Modified Layout)")

col1, col2, col3 = st.columns(3)
col1.markdown(f"<div class='kpi-card'>📈<br>Profit Margin<br>{round((df['Profit'].sum()/df['Sales'].sum())*100, 2)}%</div>", unsafe_allow_html=True)
col2.markdown(f"<div class='kpi-card'>📦<br>Total Quantity<br>{df['Quantity'].sum():,}</div>", unsafe_allow_html=True)
col3.markdown(f"<div class='kpi-card'>💰<br>Total Sales<br>${df['Sales'].sum():,}</div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# Chart Grid
# -------------------------
row1 = st.columns([1, 2])
with row1[0]:
    fig = px.pie(df, names="Category", values="Sales", title="Sales by Category", color_discrete_sequence=px.colors.sequential.Oranges)
    st.plotly_chart(fig, use_container_width=True)
with row1[1]:
    fig = px.line(df, x="Date", y="Sales", title="Sales Over Time", markers=True, color_discrete_sequence=["#e67e22"])
    st.plotly_chart(fig, use_container_width=True)

row2 = st.columns([1, 1])
with row2[0]:
    region_profit = df.groupby("Region")["Profit"].sum().reset_index()
    fig = px.bar(region_profit, x="Region", y="Profit", text_auto=True, title="Profit by Region", color_discrete_sequence=["#d35400"])
    st.plotly_chart(fig, use_container_width=True)
with row2[1]:
    fig = px.treemap(df, path=["Segment", "Category"], values="Sales", title="Sales Distribution", color_discrete_sequence=["#f39c12"])
    st.plotly_chart(fig, use_container_width=True)
