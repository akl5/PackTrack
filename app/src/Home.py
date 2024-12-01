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
            font-size: 22px;  /* Font size for the header */
            font-weight: bold;  /* Optional: make the header bold */
            color: #2a3d66;  /* Optional: change text color */
            text-decoration: underline; /* Underline the header */
        }

        /* Style for the containers with background color and rounded corners */
        .styled-container {
            background-color: #DAEEFE;  /* Background color */
            border-radius: 60px;  /* 60px rounded corners */
            padding: 20px;  /* Padding inside the container */
            height: 100%;  /* Ensure container height fits content */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Optional: slight shadow for depth */
            display: flex;  /* Use flexbox to make sure content stays inside the container */
            flex-direction: column;
            justify-content: space-around;
            text-align: left;  /* Left align the text */
            padding-left: 20px; /* Add padding to the left to align the text better */
            cursor: pointer;  /* Make the container appear clickable */
        }

        /* Style for the buttons (static buttons) inside the container */
        .styled-button {
            font-size: 14px;
            margin-top: 15px;  /* Add some space above the button */
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# ***************************************************
# The major content of this page
# ***************************************************

logger.info("Loading the Home page of the app")
st.title('PackTrack')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# ***************************************************
# Add three containers spaced evenly across the page
# ***************************************************

# :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 
#FETCHING DATA TO FRONTEND LOGIC: 
# for every row in SELECT STATEMENT (every co-op listing we can find): 
# {
# build a statement that can create code to replicate what line 80 does but col1...coln, st.columns(n)
# create a container, feed it with co-op name, company name, location, and # OF REVIEWS OF LISTING
# can be done similarly to "for object in map"
# }
# :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 :3 

<<<<<<< HEAD
if st.button('Some text on the button', 
            type = 'secondary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Professor'
    st.switch_page('pages/20_Admin_Home.py')
=======

# Create 3 columns to display the containers
col1, col2, col3 = st.columns(3)
>>>>>>> 96beee9599b0968da50fab6d902bff94aae17756

# Content for the first container (Political Strategy Advisor)
with col1:
    st.markdown(f"""
    <div class="styled-container" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
        <div class="styled-header">
            <h3>Political Strategy Advisor</h3>
        </div>
        <p>This container is for Political Strategy Advisors. Click anywhere inside to log in as John.</p>
        <div class="styled-button">
            <button>Act as John, a Political Strategy Advisor</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Content for the second container (USAID Worker)
with col2:
    st.markdown(f"""
    <div class="styled-container" onclick="window.location.href='/pages/10_USAID_Worker_Home.py';">
        <div class="styled-header">
            <h3>USAID Worker</h3>
        </div>
        <p>This container is for USAID Workers. Click anywhere inside to log in as Mohammad.</p>
        <div class="styled-button">
            <button>Act as Mohammad, an USAID Worker</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Content for the third container (System Administrator)
with col3:
    st.markdown(f"""
    <div class="styled-container" onclick="window.location.href='/pages/20_Admin_Home.py';">
        <div class="styled-header">
            <h3>System Administrator</h3>
        </div>
        <p>This container is for Administrators. Click anywhere inside to log in as SysAdmin.</p>
        <div class="styled-button">
            <button>Act as System Administrator</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ***************************************************
# End of the major content of the page
# ***************************************************
