import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme,PublicPageNav

# Apply theme settings
Theme()

# Control the sidebar content
SideBarLinks(show_home=False)
st.session_state['authenticated'] = False

PublicPageNav()