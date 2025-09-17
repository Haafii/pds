import pandas as pd
import plotly.express as px
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

# Set Streamlit page configuration
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# Function to load data from Excel
@st.cache(allow_output_mutation=True)
def get_data_from_excel():
    try:
        df = pd.read_excel(
            io="supermarkt_sales.xlsx",
            engine="openpyxl",
            sheet_name="Sales",
            skiprows=3,  # Adjust skiprows if needed
            nrows=100,   # Adjust nrows if needed
        )
        
        # Check if 'Time' column exists in the dataframe
        if 'Time' in df.columns:
            df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.time
        else:
            st.error("Error: 'Time' column not found in the Excel data.")
            st.stop()
        
        return df
    
    except FileNotFoundError:
        st.error("Error: File 'supermarkt_sales.xlsx' not found.")
        st.stop()
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.stop()

# Load data from Excel
df = get_data_from_excel()

st.sidebar.header("please filter here")
city=st.sidebar.multiselect(
    "select city",
    options=df['City'].unique(),
    default=df['City'].unique())
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["home", "about", "contact","settings"])   
if page=="home":
    df_selection=df[(df["City"].isin(city))]
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")
    total_sales = int(df_selection["Total"].sum())
    average_rating = round(df_selection["Rating"].mean(), 1)
    star_rating = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Total Sales:")
        st.subheader(f"INR {total_sales:,}")
    with middle_column:
        st.subheader("Average Rating:")
        st.subheader(f"{average_rating} {star_rating}")
    with right_column:
        st.subheader("Average Sales Per Transaction:")
        st.subheader(f"INR {average_sale_by_transaction}")
        sales_by_product_line = (df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total"))
        fig_product_sales = px.bar(
        sales_by_product_line,
        x="Total",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>Sales by Product Line</b>",
        color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
        template="plotly_white",
    )
    right_column.plotly_chart(fig_product_sales, use_container_width=True)
elif page == "about":
    st.title("About")
    st.markdown("""
    ### About This Dashboard
    This sales dashboard provides insights into supermarket sales data, 
    including sales by product lines and sales by hour.

    It is built with Streamlit and Plotly for interactive visualizations.
    The data is sourced from the 'supermarkt_sales.xlsx' Excel file.

    This app allows filtering by city, customer type, gender, and payment method.
    """)