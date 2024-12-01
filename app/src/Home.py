import streamlit as st
import logging
from modules.nav import SideBarLinks

# Set up basic logging infrastructure
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit configuration
st.set_page_config(layout='wide')

# If a user is at this page, we assume they are not authenticated.
# Change the 'authenticated' value in the streamlit session_state to false.
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control the links
# displayed on the left-side panel. 
SideBarLinks(show_home=True)

# Inject custom CSS for font sizes, background color, and rounded corners
st.markdown("""
    <style>
        /* General style for all h3 headers */
        .styled-header h3 {
            font-size: 22px;  
            font-weight: bold;  /* Optional: make the header bold */
            color: #2a3d66;  /* Optional: change text color */
            text-decoration: underline; 
        }

        /* Style for the containers with background color and rounded corners */
        .styled-container {
            background-color: #DAEEFE;  
            border-radius: 60px;  
            padding: 20px;  /* Padding inside the container */
            height: 100%; 
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
            display: flex;  
            flex-direction: column;
            justify-content: space-between;
            text-align: left;
        }

        /* Style for the buttons inside the container */
        .styled-button {
            font-size: 14px;
            margin-top: 15px;  /* Add some space above the button */
        }
    </style>
""", unsafe_allow_html=True)

# ***************************************************
# The major content of this page
# ***************************************************

logger.info("Loading the Home page of the app")
st.title('CS 3200 Sample Semester Project App')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# ***************************************************
# Add three containers spaced evenly across the page
# ***************************************************

# Create 3 columns to display the containers
col1, col2, col3 = st.columns(3)

# Content for the first container (Political Strategy Advisor)
with col1:
    st.markdown(f"""
    <div class="styled-container">
        <div class="styled-header">
            <h3>Political Strategy Advisor</h3>
        </div>
        <p>This container is for Political Strategy Advisors. Click the button below to log in as John.</p>
        <button class="styled-button" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
            Act as John, a Political Strategy Advisor
        </button>
    </div>
    """, unsafe_allow_html=True)

# Content for the second container (USAID Worker)
with col2:
    st.markdown(f"""
    <div class="styled-container">
        <div class="styled-header">
            <h3>USAID Worker</h3>
        </div>
        <p>This container is for USAID Workers. Click the button below to log in as Mohammad.</p>
        <button class="styled-button" onclick="window.location.href='/pages/10_USAID_Worker_Home.py';">
            Act as Mohammad, an USAID worker
        </button>
    </div>
    """, unsafe_allow_html=True)

# Content for the third container (System Administrator)
with col3:
    st.markdown(f"""
    <div class="styled-container">
        <div class="styled-header">
            <h3>System Administrator</h3>
        </div>
        <p>This container is for Administrators. Click the button below to log in as SysAdmin.</p>
        <button class="styled-button" onclick="window.location.href='/pages/20_Admin_Home.py';">
            Act as System Administrator
        </button>
    </div>
    """, unsafe_allow_html=True)

# ***************************************************
# End of the major content of the page
# ***************************************************
