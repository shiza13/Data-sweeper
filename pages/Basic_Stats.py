import streamlit as st

st.title("📊 Basic Statistics")

if 'data' in st.session_state:
    st.write(st.session_state['data'].describe())
else:
    st.warning("⚠️ Please upload data first from the 'Upload' page.")
