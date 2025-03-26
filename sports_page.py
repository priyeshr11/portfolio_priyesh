#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.title("Sports Interests")

# Add Sports Image
st.image("https://via.placeholder.com/300x200?text=Sports+Image", caption="My Sports Activities", use_column_width=True)

st.write("""
    - **Basketball**: I actively play basketball at the [XYZ Basketball Club](https://link-to-your-sports-club.com).
    - **Football**: I regularly participate in local football leagues, and I’m part of the [ABC FC](https://link-to-your-football-team.com).
    - **Tennis**: I enjoy playing tennis during weekends at the [Tennis Academy](https://link-to-your-tennis-academy.com).
    """)

