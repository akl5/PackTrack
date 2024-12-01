##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# Rregular and wide layout (how the controls are organized/displayed on the screen).
st.set_page_config(layout='wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# Set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('CS 3200 Sample Semester Project App')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# ***************************************************
# Add three containers spaced evenly across the page
# ***************************************************

# Create 3 columns to display the containers
col1, col2, col3 = st.columns(3)

# Content for the first container
with col1:
    st.header("Political Strategy Advisor")
    st.write("This container is for Political Strategy Advisors. Click the button below to log in as John.")
    if st.button("Act as John, a Political Strategy Advisor", 
                 type='primary', 
                 use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'pol_strat_advisor'
        st.session_state['first_name'] = 'John'
        logger.info("Logging in as Political Strategy Advisor Persona")
        st.switch_page('pages/00_Pol_Strat_Home.py')

# Content for the second container
with col2:
    st.header("USAID Worker")
    st.write("This container is for USAID Workers. Click the button below to log in as Mohammad.")
    if st.button('Act as Mohammad, an USAID worker', 
                 type='primary', 
                 use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'usaid_worker'
        st.session_state['first_name'] = 'Mohammad'
        st.switch_page('pages/10_USAID_Worker_Home.py')

# Content for the third container
with col3:
    st.header("System Administrator")
    st.write("This container is for Administrators. Click the button below to log in as SysAdmin.")
    if st.button('Act as System Administrator', 
                 type='primary', 
                 use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'administrator'
        st.session_state['first_name'] = 'SysAdmin'
        st.switch_page('pages/20_Admin_Home.py')

# ***************************************************
# End of the major content of the page
# ***************************************************
