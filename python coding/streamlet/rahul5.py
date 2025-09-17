import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# -------------------------------
# Dummy Data
# -------------------------------
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

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("Filters")
year = st.sidebar.selectbox("Select Year", options=[2022, 2023, 2024], index=1)
segment = st.sidebar.multiselect("Customer Segment", options=data["Segment"].unique(), default=data["Segment"].unique())

# Filter data
df = data.copy()
df = df[df["Segment"].isin(segment)]

# -------------------------------
# Header
# -------------------------------
st.markdown("<h1 style='color:#fff;background-color:#8B5E3C;padding:12px;border-radius:8px;'>📊 Sales Dashboard</h1>", unsafe_allow_html=True)

# -------------------------------
# KPIs
# -------------------------------
total_sales = int(df["Sales"].sum())
avg_order_value = int(df["Sales"].mean())
profit_margin = round((df["Profit"].sum() / df["Sales"].sum()) * 100, 2)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Total Sales", f"${total_sales:,}")
with col2:
    st.metric("📦 Avg Order Value", f"${avg_order_value:,}")
with col3:
    st.metric("📈 Profit Margin", f"{profit_margin}%")

# -------------------------------
# Charts Layout
# -------------------------------
col1, col2 = st.columns([2, 1])

# Sales Trend
with col1:
    fig_sales = px.line(df, x="Date", y="Sales", title="Sales Over Time", markers=True)
    st.plotly_chart(fig_sales, use_container_width=True)

# Sales by Category
with col2:
    fig_pie = px.pie(df, names="Category", values="Sales", title="Sales by Category")
    st.plotly_chart(fig_pie, use_container_width=True)

col3, col4 = st.columns([1, 1])

# Profit by Region (Bar)
with col3:
    region_profit = df.groupby("Region")[["Profit"]].sum().reset_index()
    fig_bar = px.bar(region_profit, x="Region", y="Profit", title="Profit by Region", text_auto=True)
    st.plotly_chart(fig_bar, use_container_width=True)

# Treemap
with col4:
    fig_treemap = px.treemap(df, path=["Segment", "Category"], values="Sales", title="Sales Distribution")
    st.plotly_chart(fig_treemap, use_container_width=True)

# -------------------------------
# Bottom Charts
# -------------------------------
col5, col6 = st.columns([2, 1])

# Quantity trend
with col5:
    fig_qty = px.area(df, x="Date", y="Quantity", title="Quantity Sold Over Time")
    st.plotly_chart(fig_qty, use_container_width=True)

# Profit Share
with col6:
    fig_profit_share = px.pie(df, names="Segment", values="Profit", title="Profit by Segment")
    st.plotly_chart(fig_profit_share, use_container_width=True)