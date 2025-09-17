import streamlit as st
from pyecharts.charts import Bar
from pyecharts import options as opts
import json
from pyecharts.render import make_snapshot
from streamlit.components.v1 import html

# Sample JSON data
json_data = '''
{
    "categories": ["A", "B", "C", "D"],
    "values": [10, 20, 30, 40]
}
'''

# Load JSON data
data = json.loads(json_data)
categories = data['categories']
values = data['values']

# Create a bar chart
bar = Bar()
bar.add_xaxis(categories)
bar.add_yaxis("Values", values)
bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar Chart", subtitle="From JSON Data"))

# Render chart as HTML string
chart_html = bar.render_embed()

# Display in Streamlit
st.title("📊 Pyecharts Bar Chart in Streamlit")
html(chart_html, height=500)