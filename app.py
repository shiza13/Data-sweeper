import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DataSweeper App", layout="wide")
st.title("💿 Welcome to DataSweeper")

st.write("""
**DataSweeper** is your all-in-one tool for exploring, cleaning, and visualizing data — without writing any code!

👉 First go to upload data page and start by uploading a `.csv` or `.xlsx` file.  
👉 Then, use the sidebar to go through steps like previewing your data, checking stats, cleaning messy values, analyzing specific columns, and creating beautiful visualizations.

Whether you're a beginner or a data pro, DataSweeper helps you understand your data with ease.
""")

# Add creator name centered at bottom
st.markdown("""<div style='text-align: center; padding-top: 50px; font-size: 16px;'>Created by <strong>Shiza Tariq</strong></div>""", unsafe_allow_html=True)
