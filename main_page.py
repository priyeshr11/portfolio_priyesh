#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
# from auth import login_with_google

# # Authenticate user before showing content
# if login_with_google():
#     st.title("Welcome to My Portfolio")
#     # Your content here...
# else:
#     st.stop()
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Function to display pages based on the session state
def show_page(page_name):
    st.session_state.page = page_name

# Show content based on the current page
if st.session_state.page == 'main':
        
    # Title and Header
    st.title("Priyesh's Portfolio")
    st.header("Welcome to My Personal Portfolio")
    # Add profile image
    st.image("https://via.placeholder.com/150", caption="Priyesh's Photo", width=150)
    
    # Introduction
    st.subheader("About Me")
    st.write("""
        Hello! I'm Priyesh, a passionate data scientist with a love for sports. My career focuses on solving complex data problems, 
        using machine learning to create predictive models, and telling stories through data. 
        I enjoy exploring the world of technology, but when I'm not analyzing data, you can find me on the sports field or reading about new trends in AI.
        """)
    
    # Career Interests Blog
    st.subheader("My Career Interests")
    st.write("""
        I'm deeply interested in leveraging machine learning and artificial intelligence to drive data-driven decisions.
        I enjoy working with large datasets, predictive analytics, and working on innovative tech solutions. 
        I aim to contribute to impactful projects in the tech industry, especially those that combine data science with real-world applications.
        """)
    
    # Sports Interests Blog
    st.subheader("My Sports Interests")
    st.write("""
        Sports are a huge part of my life. I believe sports teach important life lessons such as teamwork, discipline, and resilience.
        I regularly participate in basketball, football, and tennis. I aim to stay active and challenge myself in various sports, both for fitness and fun.
        """)
    
    # Add an image related to sports (e.g., a basketball image)
    st.image("https://via.placeholder.com/300x200?text=Sports+Image", caption="My Sports Interests", use_container_width=True)
    
    # Social Media Links
    st.subheader("Connect With Me")
    st.write("""
        - [LinkedIn](https://linkedin.com/in/username)
        - [GitHub](https://github.com/username)
        - [Twitter](https://twitter.com/username)
        """)
    
    # Buttons linking to other pages
    st.write("Explore More About Me:")
    
    
    # def set_page(page_name):
    #     st.session_state.page = page_name
    
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
    

elif st.session_state.page == 'education_page':
    import education_page  # assuming this is in a file called education_page.py
elif st.session_state.page == 'work_experience':
    import work_experience  # assuming this is in a file called work_experience.py
elif st.session_state.page == 'sports_page':
    import sports_page  # assuming this is in a file called sports_page.py
elif st.session_state.page == 'academics':
    import academics  # assuming this is in a file called academics.py
elif st.session_state.page == 'research_work':
    import research_work  # assuming this is in a file called research_work.py    
    
    
