import streamlit as st
import pandas as pd

st.title("📌 Column-wise Analysis")

if 'data' in st.session_state:
    df = st.session_state['data']
    column = st.selectbox("Select a column", df.columns)

    if pd.api.types.is_numeric_dtype(df[column]):
        st.write("Mean:", df[column].mean())
        st.write("Max:", df[column].max())
        st.write("Min:", df[column].min())
    else:
        st.write(df[column].value_counts())
else:
    st.warning("⚠️ Please upload data first from the 'Upload' page.")
