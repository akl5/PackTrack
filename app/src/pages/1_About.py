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

st.write("# About this App")

st.markdown (
    """
    This is an unfinished page for PackTrack. 

    The goal of this demo is to provide more information about PackTrack and the benefits that we offer to students as a platform. 

    Stay tuned for more information and features to come!
    """
        )