#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.title("Academic Experience")

# Add Academic Image
st.image("https://via.placeholder.com/300x200?text=Academic+Experience", caption="My Academic Experience", use_column_width=True)

st.subheader("Research Assistant - Data Science")
st.write("""
    University of ABC, September 2023 - Present
    - Assisted in research on applying machine learning models to analyze climate data.
    - Worked on papers related to predictive analytics for environmental forecasting.
    """)

