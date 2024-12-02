import streamlit as st
import logging
from modules.nav import SideBarLinks, Theme


# Set up basic logging infrastructure
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Streamlit configuration
st.set_page_config(layout='wide')


# If a user is at this page, we assume they are not authenticated.
# Change the 'authenticated' value in the streamlit session_state to false.
st.session_state['authenticated'] = False


# Apply theme settings
Theme()


# Use the SideBarLinks function from modules/nav.py to control the links
# displayed on the left-side panel.
SideBarLinks(show_home=False)  # This hides the "Home" link in the sidebar


# The login button
st.markdown("""
<div style="display: flex; justify-content: flex-end; align-items: center; margin-bottom: 20px;">
   <a href="/login" style="text-decoration: none; background-color: #3E4B8B; color: white;
      padding: 10px 20px; border-radius: 10px; font-size: 16px; font-weight: bold;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
       Login
   </a>
</div>
""", unsafe_allow_html=True)


# The rest of your content...
st.markdown("""
   <style>
       /* General style for all h3 headers */
       .styled-header h3 {
           font-size: 22px;  /* Font size for the header */
           font-weight: light;  /* Optional: make the header bold */
           text-decoration: underline; /* Underline the header */
       }


       /* Style for the containers with background color and rounded corners */
       .styled-container {
           background-color: #DAEEFE;  /* Background color */
           border-radius: 60px;  /* 60px rounded corners */
           padding: 10%;  /* Padding inside the container */
           width: 18rem;
           height: 18rem;  /* Ensure container height fits content */
           box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Optional: slight shadow for depth */
           display: flex;  /* Use flexbox to make sure content stays inside the container */
           justify-content: center;
           flex-direction: column;
           text-align: left;  /* Left align the text */
           padding-left: 2rem; /* Add padding to the left to align the text better */
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


# The major content of this page
logger.info("Loading the Home page of the app")
st.title('CS 3200 Sample Semester Project App')
st.write('\n\n')
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: right;">
   <a href="/pages/CO_OP_Listings" style="text-decoration: none; color: #3E4B8B;">
       <h3>View CO-OP Listings</h3>
   </a>
   <a href="/pages/Latest_Reviews" style="text-decoration: none; color: #3E4B8B;">
       <h3>View Latest Reviews</h3>
   </a>
</div>
""", unsafe_allow_html=True)


# Create 3 columns to display the containers
col1, col2, col3 = st.columns(3)


# Content for the first container (Political Strategy Advisor)
with col1:
   st.markdown(f"""
   <div class="styled-container" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
       <div class="styled-header">
           <h3>CO-OP Review</h3>
       </div>
       <p>This container is an Example CO-OP Review. Click anywhere inside to log in as John.</p>
       <div class="number-of-reviews">
           <h5> 3 Reviews </h5>
       </div>
   </div>
   """, unsafe_allow_html=True)


# Content for the second container (USAID Worker)
with col2:
   st.markdown(f"""
   <div class="styled-container" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
       <div class="styled-header">
           <h3>CO-OP Review</h3>
       </div>
       <p>This container is an Example CO-OP Review. Click anywhere inside to log in as John.</p>
       <div class="number-of-reviews">
           <h5> 3 Reviews </h5>
       </div>
   </div>
   """, unsafe_allow_html=True)


# Content for the third container (System Administrator)
with col3:
   st.markdown(f"""
   <div class="styled-container" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
       <div class="styled-header">
           <h3>CO-OP Review</h3>
       </div>
       <p>This container is an Example CO-OP Review. Click anywhere inside to log in as John.</p>
       <div class="number-of-reviews">
           <h5> 3 Reviews </h5>
       </div>
   </div>
   """, unsafe_allow_html=True)


# Darker blue background section
st.markdown("""
<div style="background-color: #DBEFFF; color: #3E4B8B; padding: 40px 0; margin-top: 20px; text-align: center; width: 100vw; position: relative; left: 50%; transform: translateX(-50%);">
    <h2>View Roles with Latest Reviews</h2>
    <p>Users Will Go Below</p>
    <div style="display: flex; justify-content: center; margin-top: 30px; gap: 20px; max-width: 80%; margin: 0 auto;">
        <!-- First Container -->
        <div style="background-color: white; color: #3E4B8B; border-radius: 10px; text-align: left; padding: 20px; width: 300px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="margin: 0;">John Doe</h3>
            <p style="margin: 5px 0;">Degree: Bachelor of Computer Science</p>
            <p style="margin: 5px 0;">Internship: Software Developer</p>
            <p style="margin: 5px 0;">Description: Worked on full-stack application development and database design.</p>
        </div>
        <!-- Second Container -->
        <div style="background-color: white; color: #3E4B8B; border-radius: 10px; text-align: left; padding: 20px; width: 300px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="margin: 0;">Jane Smith</h3>
            <p style="margin: 5px 0;">Degree: Master of Data Science</p>
            <p style="margin: 5px 0;">Internship: Data Analyst</p>
            <p style="margin: 5px 0;">Description: Conducted data analysis and visualization to drive business decisions.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)







# End of the major content of the page

