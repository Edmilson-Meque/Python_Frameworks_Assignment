import streamlit as st
import pandas as pd

st.title("Python Frameworks Assignment")
st.write("This is a simple Streamlit app using Pandas.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())

    st.write("Summary Statistics:")
    st.write(df.describe())

    st.write("Columns with missing values:")
    st.write(df.isnull().sum())

# Simple interaction example
st.write("Select a column to see its unique values:")
if uploaded_file:
    column = st.selectbox("Select column", df.columns)
    st.write(df[column].unique())
