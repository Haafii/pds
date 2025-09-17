import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# --------------------------
# Dummy Data
# --------------------------
dates = pd.date_range("2023-01-01", periods=365)
data = pd.DataFrame({
    "Date": dates,
    "Year": dates.year,
    "Month": dates.month,
    "Sales": np.random.randint(1000, 10000, size=365),
    "Profit": np.random.randint(200, 3000, size=365),
    "Sale_Type": np.random.choice(["Online", "Offline", "Wholesale"], size=365),
    "Payment_Mode": np.random.choice(["Card", "Cash", "UPI", "Wallet"], size=365),
    "Category": np.random.choice(["Electronics", "Clothing", "Groceries", "Furniture"], size=365),
    "Product": np.random.choice(["P1","P2","P3","P4","P5"], size=365)
})

# --------------------------
# Sidebar Filters
# --------------------------
st.sidebar.header("Filters")
year = st.sidebar.selectbox("Select Year", sorted(data["Year"].unique()))
sale_type = st.sidebar.multiselect("Sale Type", data["Sale_Type"].unique(), default=data["Sale_Type"].unique())
pay_mode = st.sidebar.multiselect("Payment Mode", data["Payment_Mode"].unique(), default=data["Payment_Mode"].unique())

# Filter data
df = data[(data["Year"] == year) & (data["Sale_Type"].isin(sale_type)) & (data["Payment_Mode"].isin(pay_mode))]

# --------------------------
# KPI Section
# --------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
profit_pct = round((total_profit / total_sales) * 100, 2)

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Sales", f"${total_sales:,.0f}")
kpi2.metric("Total Profit", f"${total_profit:,.0f}")
kpi3.metric("Profit %", f"{profit_pct}%")

st.markdown("---")

# --------------------------
# Charts Layout
# --------------------------
col1, col2, col3 = st.columns([2,1,1])

# Monthly sales bar chart
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
col1.plotly_chart(px.bar(monthly_sales, x="Month", y="Sales", title="Monthly Sales"), use_container_width=True)

# Sale Type Pie
col2.plotly_chart(px.pie(df, names="Sale_Type", values="Sales", title="Sale Type Distribution"), use_container_width=True)

# Payment Mode Pie
col3.plotly_chart(px.pie(df, names="Payment_Mode", values="Sales", title="Payment Mode"), use_container_width=True)

st.markdown("---")

# Daily Sales Trend
st.plotly_chart(px.area(df, x="Date", y="Sales", title="Daily Sales Trend"), use_container_width=True)

st.markdown("---")

# Bottom section: Categories + Products
col4, col5 = st.columns([1,1])

# TreeMap for Categories
col4.plotly_chart(px.treemap(df, path=["Category"], values="Sales", title="Sales by Category"), use_container_width=True)

# Top Products Table
top_products = df.groupby("Product")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False).reset_index()
col5.subheader("Top Products")
st.dataframe(top_products, use_container_width=True)