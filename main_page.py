# #!/usr/bin/env python
# # coding: utf-8

# # In[ ]:


# import streamlit as st
# # from auth import login_with_google

# # # Authenticate user before showing content
# # if login_with_google():
# #     st.title("Welcome to My Portfolio")
# #     # Your content here...
# # else:
# #     st.stop()

import streamlit as st

# Initialize session state for page if not present
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Function to display pages based on session state
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

    # Buttons to navigate to different pages
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

# Work Experience page
elif st.session_state.page == 'work_experience':
    st.title("Work Experience")
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

    # Buttons to navigate to different pages
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("Home", on_click=show_page, args=("main",))
    with col2:
        st.button("Education", on_click=show_page, args=("education_page",))
    with col3:
        st.button("Sports Interest", on_click=show_page, args=("sports_page",))
    with col4:
        st.button("Academic Experience", on_click=show_page, args=("academics",))
    with col5:
        st.button("Research Projects", on_click=show_page, args=("research_work",))

# Education page
elif st.session_state.page == 'education_page':
    st.title("Education")
    st.image("https://via.placeholder.com/300x200?text=Education", caption="My Education Background", use_container_width=True)
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

    # Buttons to navigate to different pages
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("Home", on_click=show_page, args=("main",))
    with col2:
        st.button("Work Experience", on_click=show_page, args=("work_experience",))
    with col3:
        st.button("Sports Interest", on_click=show_page, args=("sports_page",))
    with col4:
        st.button("Academic Experience", on_click=show_page, args=("academics",))
    with col5:
        st.button("Research Projects", on_click=show_page, args=("research_work",))

# Repeat similar structure for other pages like 'sports_page', 'academics', etc.
elif st.session_state.page == 'sports_page':
    st.title("Sports Interests")

# Add Sports Image
    st.image("https://via.placeholder.com/300x200?text=Sports+Image", caption="My Sports Activities", use_container_width=True)
    
    st.write("""
        - **Basketball**: I actively play basketball at the [XYZ Basketball Club](https://link-to-your-sports-club.com).
        - **Football**: I regularly participate in local football leagues, and I’m part of the [ABC FC](https://link-to-your-football-team.com).
        - **Tennis**: I enjoy playing tennis during weekends at the [Tennis Academy](https://link-to-your-tennis-academy.com).
        """)
        # Buttons to navigate to different pages
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("Home", on_click=show_page, args=("main",))
    with col2:
        st.button("Education", on_click=show_page, args=("education_page",))
    with col3:
        st.button("Work Experience", on_click=show_page, args=("work_experience",))
    with col4:
        st.button("Academic Experience", on_click=show_page, args=("academics",))
    with col5:
        st.button("Research Projects", on_click=show_page, args=("research_work",))
        
elif st.session_state.page == 'academics':
    st.title("Academic Experience")
    
    # Add Academic Image
    st.image("https://via.placeholder.com/300x200?text=Academic+Experience", caption="My Academic Experience", use_container_width=True)
    
    st.subheader("Research Assistant - Data Science")
    st.write("""
        University of ABC, September 2023 - Present
        - Assisted in research on applying machine learning models to analyze climate data.
        - Worked on papers related to predictive analytics for environmental forecasting.
        """)

        # Buttons to navigate to different pages
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("Home", on_click=show_page, args=("main",))
    with col2:
        st.button("Education", on_click=show_page, args=("education_page",))
    with col3:
        st.button("Work Experience", on_click=show_page, args=("work_experience",))
    with col4:
        st.button("Sports Interest", on_click=show_page, args=("sports_page",))
    with col5:
        st.button("Research Projects", on_click=show_page, args=("research_work",))


elif st.session_state.page == 'research_work':
    
    st.title("Research Projects")
    
    # Add Research Image
    st.image("https://via.placeholder.com/300x200?text=Research+Projects", caption="My Research Projects", use_container_width=True)
    
    st.subheader("Predictive Analytics for Sales Forecasting")
    st.write("""
        This project focused on building a model to predict sales based on historical data using regression techniques.
        """)
    
    st.subheader("Customer Segmentation with Machine Learning")
    st.write("""
        A machine learning project using K-means clustering to identify customer groups based on purchasing behavior.
        """)
            # Buttons to navigate to different pages
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.button("Home", on_click=show_page, args=("main",))
    with col2:
        st.button("Education", on_click=show_page, args=("education_page",))
    with col3:
        st.button("Work Experience", on_click=show_page, args=("work_experience",))
    with col4:
        st.button("Sports Interest", on_click=show_page, args=("sports_page",))
    with col5:
        st.button("Academic Experience", on_click=show_page, args=("academics",))
