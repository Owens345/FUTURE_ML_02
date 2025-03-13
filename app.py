import streamlit as st
import pandas as pd

st.title("Movie Revenue Prediction")
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
