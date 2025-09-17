import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ---------------------------
# Backend API configuration
# ---------------------------
API_BASE = "http://localhost:5001"  # Flask backend URL

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard (Streamlit + Flask API)")

st.markdown("This dashboard connects to the Flask API running at port `5001`.")

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("Filters")

source = st.sidebar.selectbox("Data Source", ["xlsx", "sql"])
product = st.sidebar.text_input("Product")
city = st.sidebar.text_input("City")
gender = st.sidebar.selectbox("Gender", ["", "Male", "Female"])
payment = st.sidebar.text_input("Payment")
limit = st.sidebar.number_input("Limit", min_value=0, value=0)
offset = st.sidebar.number_input("Offset", min_value=0, value=0)

if st.sidebar.button("Fetch Data"):
    params = {"source": source}
    if product:
        params["product"] = product
    if city:
        params["city"] = city
    if gender:
        params["gender"] = gender
    if payment:
        params["payment"] = payment
    if limit > 0:
        params["limit"] = limit
    if offset > 0:
        params["offset"] = offset

    try:
        resp = requests.get(f"{API_BASE}/api/sales", params=params, timeout=20)
        if resp.status_code == 200:
            data = resp.json()
            if not data:
                st.warning("No records found with these filters.")
            else:
                df = pd.DataFrame(data)
                st.success(f"Fetched {len(df)} records from API ✅")

                # Show raw dataframe
                st.dataframe(df, use_container_width=True)

                # ---------------------------
                # Plotly Visualizations
                # ---------------------------
                st.subheader("Visualizations")

                # 1. Bar chart - Total sales by product
                if "Product line" in df.columns and "Total" in df.columns:
                    fig1 = px.bar(df.groupby("Product", as_index=False)["Total"].sum(),
                                  x="Product", y="Total", title="Total Sales by Product")
                    st.plotly_chart(fig1, use_container_width=True)

                # 2. Pie chart - Payment method distribution
                if "Payment" in df.columns and "Total" in df.columns:
                    fig2 = px.pie(df, names="Payment", values="Total",
                                  title="Sales Distribution by Payment Method")
                    st.plotly_chart(fig2, use_container_width=True)

                # 3. Time series - Sales over time
                for col in ["Date", "Invoice Date", "date"]:
                    if col in df.columns:
                        try:
                            df[col] = pd.to_datetime(df[col])
                            fig3 = px.line(df, x=col, y="Total", color="City",
                                           title=f"Sales over Time ({col})", markers=True)
                            st.plotly_chart(fig3, use_container_width=True)
                        except Exception:
                            pass
                        break

        else:
            st.error(f"API request failed ({resp.status_code}): {resp.text}")

    except Exception as e:
        st.error(f"Could not connect to API: {e}")
