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
    st.session_state['role'] = 'coop_manager'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    # landing page for this particular user type
    logger.info("Logging in Co-Op Manager..")
    st.switch_page('pages/00_Pol_Strat_Home.py')

if st.button('Act as Mohammad, an USAID worker', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'usaid_worker'
    st.switch_page('pages/10_USAID_Worker_Home.py')

if st.button('Act as System Administrator', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.switch_page('pages/20_Admin_Home.py')