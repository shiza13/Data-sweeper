import streamlit as st
import pandas as pd
from data_store import save_uploaded_data

st.title("📁 Upload CSV or XLSX File")

# File uploader widget to upload CSV or XLSX file
file = st.file_uploader("Upload your file here", type=["csv", "xlsx"])

if file:
    # Save the uploaded file to session state
    save_uploaded_data(file)

    # Read the uploaded file into a DataFrame (directly handled inside save_uploaded_data)
    st.success("✅ File uploaded and stored successfully! Use the sidebar to continue.")
    
    # You can also show the uploaded data for preview (optional)
    if "data" in st.session_state:
        st.subheader("📊 Uploaded Data Preview")
        st.dataframe(st.session_state["data"])
