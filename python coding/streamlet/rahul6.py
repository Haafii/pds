import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("supermarkt_sales.csv")  # replace with your file
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filter Data")

city = st.sidebar.multiselect(
    "Select City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

# -----------------------------
# Main Dashboard
# -----------------------------
st.title("📊 Sales Dashboard")
st.markdown("### Key Performance Indicators")

# KPIs
total_sales = int(df_selection["Total"].sum())
avg_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(avg_rating, 0))
avg_sale_by_txn = round(df_selection["Total"].mean(), 2)

left, middle, right = st.columns(3)
with left:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle:
    st.subheader("Average Rating:")
    st.subheader(f"{avg_rating} {star_rating}")
with right:
    st.subheader("Average Sale per Transaction:")
    st.subheader(f"US $ {avg_sale_by_txn}")

st.markdown("---")

# -----------------------------
# Charts
# -----------------------------
# Sales by Product Line
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

# Sales by Hour
sales_by_hour = df_selection.groupby(df_selection["Time"].dt.hour).sum()[["Total"]]
fig_hourly_sales = px.line(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by Hour</b>",
    template="plotly_white"
)

# Pie Chart - Payment Method
fig_payment = px.pie(
    df_selection,
    names="Payment",
    values="Total",
    title="Payment Method Share"
)

# Treemap - Branch vs Product Line
fig_treemap = px.treemap(
    df_selection,
    path=["Branch", "Product line"],
    values="Total",
    title="Sales Breakdown (Branch → Product Line)"
)

# -----------------------------
# Layout
# -----------------------------
left_col, right_col = st.columns(2)
left_col.plotly_chart(fig_product_sales, use_container_width=True)
right_col.plotly_chart(fig_hourly_sales, use_container_width=True)

left_col2, right_col2 = st.columns(2)
left_col2.plotly_chart(fig_payment, use_container_width=True)
right_col2.plotly_chart(fig_treemap, use_container_width=True)
