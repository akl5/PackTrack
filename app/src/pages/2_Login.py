import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme

Theme()
SideBarLinks()

if st.button("Log in as Co-Op Manager", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'coopmanager'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    # landing page for this particular user type
    logger.info("Logging in Co-Op Manager...")
    st.switch_page('pages/5_CoopManager_Dashboard.py')

if st.button('Log in as Company Representative', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'usaid_worker'
    logger.info("Logging in Company Representative...")
    st.switch_page('pages/6_Company_Representative.py')

if st.button('Log in as System Administrator', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.switch_page('pages/7_System_Admin_Dashboard.py')
