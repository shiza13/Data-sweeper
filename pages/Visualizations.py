import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Data Visualizations")

if 'data' in st.session_state:
    df = st.session_state['data']

    st.subheader("Select a column to visualize")
    column = st.selectbox("Choose a column", df.columns)

    chart_type = st.radio("Choose chart type", ["Line Chart", "Histogram", "Value Counts (Bar)"])

    if chart_type == "Line Chart":
        if pd.api.types.is_numeric_dtype(df[column]):
            st.line_chart(df[column])
        else:
            st.warning("Line charts require numeric data.")

    elif chart_type == "Histogram":
        if pd.api.types.is_numeric_dtype(df[column]):
            fig, ax = plt.subplots()
            ax.hist(df[column].dropna(), bins=20, color='skyblue', edgecolor='black')
            st.pyplot(fig)
        else:
            st.warning("Histogram works only with numeric columns.")

    elif chart_type == "Value Counts (Bar)":
        counts = df[column].value_counts()
        fig, ax = plt.subplots()
        counts.plot(kind='bar', ax=ax, color='orange')
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        st.pyplot(fig)
else:
    st.warning("⚠️ Please upload data first from the 'Upload' page.")
