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
    Our project is PackTrack, a web application that is intended to enhance the current co-op search tool NUworks at Northeastern University.
    On top of the existing NUworks functionality, PackTrack enables students* to provide objective feedback for co-op positions they have worked at. This feedback system, in turn, provides employees at said job and other Northeastern students with valuable insights into the reality of working the respective role at said company. Companies can then make changes to their positions so that they become more enticing to future applicants by generating better reviews/feedback from other students. 
    """
        )