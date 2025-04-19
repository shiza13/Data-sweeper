import pandas as pd
import streamlit as st

def save_uploaded_data(file):
    """Function to save uploaded data to session state."""
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.session_state['data'] = df  # Store the dataframe in session state
    st.session_state['uploaded'] = True  # Flag to mark the data as uploaded
