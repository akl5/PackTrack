import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme

Theme()
SideBarLinks()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Park+Sans&display=swap');

    body {
        font-family: 'Park Sans', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Park Sans', sans-serif;
    }

    .stButton, .stTextInput, .stTextArea, .stSelectbox, .stSlider, .stRadio, .stCheckbox, .stDateInput, .stNumberInput {
        font-family: 'Park Sans', sans-serif;
    }

    label, .stLabel, .stText {
        font-family: 'Park Sans', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("# Accessing a REST API from Within Streamlit")

"""
Simply retrieving data from a REST api running in a separate Docker Container.

If the container isn't running, this will be very unhappy.  But the Streamlit app 
should not totally die. 
"""
data = {} 
try:
  data = requests.get('http://api:4000/p/products').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)
