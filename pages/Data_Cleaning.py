import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaning")

# Check if data is uploaded and available in session state
if "data" not in st.session_state or not st.session_state.get("uploaded", False):
    st.warning("📂 Please upload your data first from the Upload page.")
else:
    df = st.session_state['data']  # Access the uploaded data from session state

    # Display file name for clarity
    filename = st.session_state.get('filename', 'Unknown File')
    st.subheader(f"🎯 Cleaning Data for `{filename}`")

    # Let the user choose a cleaning operation
    clean_option = st.radio(
        "Select a data cleaning option:",
        ("Remove duplicates", "Fill missing values"),
        horizontal=True
    )

    if clean_option == "Remove duplicates":
        before = df.shape[0]
        df.drop_duplicates(inplace=True)
        after = df.shape[0]
        st.success(f"✅ Removed {before - after} duplicate rows.")

    elif clean_option == "Fill missing values":
        # Handle missing values for numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        non_numeric_cols = df.select_dtypes(exclude=['number']).columns

        # For numeric columns: fill missing values with the mean
        for col in numeric_cols:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].mean(), inplace=True)

        # For non-numeric columns: fill missing values with "Missing"
        for col in non_numeric_cols:
            if df[col].isnull().sum() > 0:
                df[col].fillna("Missing", inplace=True)

        st.success("✅ Missing values filled!")

    # Show cleaned data preview
    st.subheader("📊 Cleaned Data Preview")
    st.dataframe(df)

    # Option to delete the cleaned data
    if st.button("Delete Cleaned Data"):
        del st.session_state["data"]  # Remove the cleaned data from session state
        st.session_state['uploaded'] = False  # Reset the uploaded flag
        st.success("✅ Cleaned data has been deleted!")

    # Save the cleaned data back to session state
    st.session_state['data'] = df
