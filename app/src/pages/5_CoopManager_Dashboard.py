import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme

# Apply theme settings
Theme()

# Control the sidebar content
SideBarLinks(show_home=False)

st.write("## Welcome Co-op Manager!")

if st.button("View All Active Co-op Listings"):
    st.switch_page("pages/8_All_Active_Listings.py")

if st.button("View All Listings By Date"):
    st.switch_page("pages/9_Listings_By_Date.py")