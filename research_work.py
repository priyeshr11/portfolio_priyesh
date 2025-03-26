#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.title("Research Projects")

# Add Research Image
st.image("https://via.placeholder.com/300x200?text=Research+Projects", caption="My Research Projects", use_column_width=True)

st.subheader("Predictive Analytics for Sales Forecasting")
st.write("""
    This project focused on building a model to predict sales based on historical data using regression techniques.
    """)

st.subheader("Customer Segmentation with Machine Learning")
st.write("""
    A machine learning project using K-means clustering to identify customer groups based on purchasing behavior.
    """)

