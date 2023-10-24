import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Analysis")

col1, col2, col3 = st.columns(3)
col1.metric("Name", 'a')
col2.metric('Marks', 82)

df = pd.read_csv('data.csv')
# df1 = df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'], axis='columns')

if st.sidebar.button('load dataset'):
    st.write(df)

if st.sidebar.button('load description'):
    st.write(df.describe())
    
if st.sidebar.button('load barchart'):
    df2=df.head(20)
    fig = plt.figure(figsize=(10,8))
    plt.bar(df2['Product'], df2['Qty'])
    st.pyplot(fig)    

