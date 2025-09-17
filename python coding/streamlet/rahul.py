import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Dummy Data
dates = pd.date_range("2023-01-01", periods=365)
data = pd.DataFrame({
    "Date": dates,
    "Year": dates.year,
    "Sales": np.random.randint(1000, 10000, size=365),
    "Profit": np.random.randint(200, 3000, size=365),
    "Sale_Type": np.random.choice(["Online", "Offline", "Wholesale"], size=365),
    "Payment_Mode": np.random.choice(["Card", "Cash", "UPI", "Wallet"], size=365),
    "Category": np.random.choice(["Electronics", "Clothing", "Groceries", "Furniture"], size=365),
})

# Filters
year = st.sidebar.selectbox("Year", sorted(data["Year"].unique()))
df = data[data["Year"] == year]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Profit %", f"{round((df['Profit'].sum()/df['Sales'].sum())*100,2)}%")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Monthly Sales", "Daily Trend", "Sale Type", "Payment Mode", "Categories"])

with tab1:
    fig = px.bar(df.groupby(df["Date"].dt.month)["Sales"].sum().reset_index(), x="Date", y="Sales", title="Monthly Sales")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.plotly_chart(px.area(df, x="Date", y="Sales", title="Daily Sales"), use_container_width=True)

with tab3:
    st.plotly_chart(px.pie(df, names="Sale_Type", values="Sales"), use_container_width=True)

with tab4:
    st.plotly_chart(px.pie(df, names="Payment_Mode", values="Sales"), use_container_width=True)

with tab5:
    st.plotly_chart(px.treemap(df, path=["Category"], values="Sales"), use_container_width=True)
