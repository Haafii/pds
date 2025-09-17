import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from st_aggrid import AgGrid

# Dummy Data
dates = pd.date_range("2023-01-01", periods=365)
data = pd.DataFrame({
    "Date": dates,
    "Year": dates.year,
    "Sales": np.random.randint(1000, 10000, size=365),
    "Profit": np.random.randint(200, 3000, size=365),
    "Product": np.random.choice(["P1", "P2", "P3", "P4"], size=365),
})

# Filter
year = st.sidebar.selectbox("Year", sorted(data["Year"].unique()))
df = data[data["Year"] == year]

# KPIs
st.metric("Total Sales", f"${df['Sales'].sum():,.0f}")

# Charts
st.plotly_chart(px.area(df, x="Date", y="Sales", title="Daily Sales"), use_container_width=True)

# AgGrid Table
st.subheader("Interactive Product Sales Table")
top_products = df.groupby("Product")[["Sales", "Profit"]].sum().reset_index()
AgGrid(top_products)
