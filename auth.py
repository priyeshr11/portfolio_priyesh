#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# auth.py
import streamlit as st
from streamlit_oauth import OAuth

def login_with_google():
    oauth = OAuth("google")

    if oauth.is_logged_in():
        user_info = oauth.get_user_info()
        st.session_state["user_email"] = user_info["email"]
        return True
    else:
        oauth.login("Login with Google")
        return False

