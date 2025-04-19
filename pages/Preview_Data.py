import streamlit as st

st.title("🔍 Data Preview")

if 'data' in st.session_state:
    st.dataframe(st.session_state['data'], use_container_width=True)
else:
    st.warning("⚠️ Please upload data first from the 'Upload' page.")
