import streamlit as st
import pandas as pd

st.title("🔁 Convert Column Types")

if 'data' in st.session_state:
    df = st.session_state['data'].copy()
    column = st.selectbox("Select a column to convert", df.columns)
    conversion_type = st.radio("Convert to:", ["Numeric", "String", "Datetime"])

    if st.button("Convert"):
        try:
            if conversion_type == "Numeric":
                df[column] = pd.to_numeric(df[column], errors='coerce')
            elif conversion_type == "String":
                df[column] = df[column].astype(str)
            elif conversion_type == "Datetime":
                df[column] = pd.to_datetime(df[column], errors='coerce')
            st.session_state['data'] = df
            st.success(f"Column '{column}' converted to {conversion_type}.")
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.warning("⚠️ Please upload data first from the 'Upload' page.")
