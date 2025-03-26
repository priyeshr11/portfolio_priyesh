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


st.write("Explore More About Me:")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("Education", on_click=show_page, args=("education_page",))
with col2:
    st.button("Work Experience", on_click=show_page, args=("work_experience",))
with col3:
    st.button("Sports Interest", on_click=show_page, args=("sports_page",))
with col4:
    st.button("Academic Experience", on_click=show_page, args=("academics",))
with col5:
    st.button("Research Projects", on_click=show_page, args=("research_work",))
