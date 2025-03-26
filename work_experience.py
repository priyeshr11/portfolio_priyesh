#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("Work Experience")

# Add Work Experience Image
st.image("https://via.placeholder.com/300x200?text=Work+Experience", caption="My Work Experience", use_column_width=True)

st.subheader("Data Analyst Intern")
st.write("""
    Company ABC, June 2023 - August 2023
    - Developed data pipelines for automated data extraction and transformation.
    - Built dashboards using Tableau and Power BI for business metrics visualization.
    """)

st.subheader("Junior Data Scientist")
st.write("""
    Tech Solutions, September 2022 - May 2023
    - Created customer segmentation models using K-means clustering.
    - Worked on cleaning and processing data for ML models.
    """)


# In[ ]:




