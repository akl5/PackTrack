import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This is a an unfinished page for PackTrack. 

    The goal of this demo is to provide more information about PackTrack and the benefits that we offer to students as a platform. 

    Stay tuned for more information and features to come!
    """
        )