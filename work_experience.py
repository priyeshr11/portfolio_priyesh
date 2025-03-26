#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("Work Experience")
    
    # Add Work Experience Image
st.image("https://via.placeholder.com/300x200?text=Work+Experience", caption="My Work Experience", use_container_width=True)
    
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
    
def set_page(page_name):
    st.session_state.page = page_name
    col1, col2, col3, col4, col5 = st.columns(5)
    	with col1:
        	st.button("Education", on_click=set_page, args=("education_page",))
   	with col2:
        	st.button("Home", on_click=set_page, args=("main_page",))
	with col3:
		st.button("Sports Interest", on_click=set_page, args=("sports_page",))
	with col4:
        	st.button("Academic Experience", on_click=set_page, args=("academics",))
	with col5:
        	st.button("Research Projects", on_click=set_page, args=("research_work",))
  
