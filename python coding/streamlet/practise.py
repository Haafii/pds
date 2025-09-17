import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("/Users/anusreev/Desktop/python coding/streamlet/weather.csv")   # Use your uploaded file
st.title("Weather Visualization Dashboard 🌦️")
st.write("Dataset (from CSV):")
st.dataframe(data.head())

st.sidebar.subheader("Settings")
columns = data.columns.tolist()

x_axis = st.sidebar.selectbox("Select X-axis", columns)
y_axis = st.sidebar.selectbox("Select Y-axis", columns)

option = st.sidebar.selectbox(
    "Choose Graph",
    ["Line Chart", "Scatter Plot", "Bar Chart", "Pie Chart"]
)

if option == "Line Chart":
    fig = px.line(data, x=x_axis, y=y_axis, title=f"Line Chart of {y_axis} vs {x_axis}", markers=True)
    st.plotly_chart(fig)

elif option == "Scatter Plot":
    fig = px.scatter(data, x=x_axis, y=y_axis, size=data[y_axis], 
                     color=data[x_axis], title=f"Scatter Plot of {y_axis} vs {x_axis}")
    st.plotly_chart(fig)

elif option == "Bar Chart":
    fig = px.bar(data, x=x_axis, y=y_axis, color=y_axis,
                 title=f"Bar Chart of {y_axis} vs {x_axis}", text=y_axis)
    st.plotly_chart(fig)

elif option == "Pie Chart":
    fig = px.pie(data, names=x_axis, values=y_axis, title=f"Pie Chart of {y_axis} by {x_axis}")
    st.plotly_chart(fig)

st.sidebar.markdown("---")
st.sidebar.subheader("Q&A")

st.sidebar.write("**a. Why Streamlit for Data Science?**")
st.sidebar.write("- Easy to create interactive dashboards\n"
                 "- Supports charts (Plotly, Matplotlib, Echarts)\n"
                 "- Deploy quickly without web development knowledge")

st.sidebar.write("**b. Why venv for Streamlit?**")
st.sidebar.write("- Keeps project dependencies isolated\n"
                 "- Avoids version conflicts\n"
                 "- Makes sharing projects easier")

st.sidebar.write("**c. Steps to create virtual environment**")
st.sidebar.code("""
1. python -m venv myenv
2. source myenv/bin/activate   # (Linux/Mac)
   myenv\\Scripts\\activate    # (Windows)
3. pip install streamlit plotly pandas
4. streamlit run app.py
""")
