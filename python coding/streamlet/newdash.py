import pandas as pd
import plotly.express as px
import streamlit as st
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="fake news", page_icon=":bar_chart:", layout="wide")

@st.cache(allow_output_mutation=True)
def get_data_from_csv():
    try:
        df = pd.read_csv(
            "Fake.csv",
            skiprows=3,
            nrows=100
        )
        return df
    except FileNotFoundError:
        st.error("Error: File 'Fake.csv' not found.")
        st.stop()

df = get_data_from_csv()

# --- Sidebar ---
st.sidebar.header("Please Filter Here:")

# Column selection
columns_selected = st.sidebar.multiselect(
   "Select Columns to Display",
    options=["title", "text", "subject", "date"],
    default=["title", "subject"]
)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Settings"])

# --- Pages ---
if page == "Home":
    # Show only selected columns
    df_selection = df[columns_selected]
    st.dataframe(df_selection)

elif page == "About":
    st.subheader("About")
    st.write("This is a Fake News dataset explorer app built with Streamlit.")

elif page == "Contact":
    st.subheader("Contact")
    st.write("📧 Email: yourname@example.com")

elif page == "Settings":
    st.subheader("Settings")
    st.write("⚙️ Customize your app settings here.")
