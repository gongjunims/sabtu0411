import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Visualisasi Data Diamond")
st.write("by arin ^__^")

df = pd.read_csv("data/diamonds.csv")

st.write("## 5 Data Pertama tentang Diamonds") 
st.write(df.head() )

st.write("## Data Harga Diamonds")
plot = px.histogram(
    df, 
    x = "price",
    title = "Histogram Harga Diamonds" 