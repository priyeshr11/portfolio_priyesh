#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.title("Education")

# Add Education Image
st.image("https://via.placeholder.com/300x200?text=Education", caption="My Education Background", use_column_width=True)

st.subheader("Master of Science in Data Science")
st.write("""
    University of ABC, 2022 - 2024
    Relevant Courses: Machine Learning, Big Data Analytics, Data Visualization, Statistical Methods for Data Science
    """)

st.subheader("Bachelor of Technology in Computer Science")
st.write("""
    University of XYZ, 2018 - 2022
    Relevant Courses: Algorithms, Data Structures, Database Management Systems, Programming Languages
    """)

