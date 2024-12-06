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

# API endpoint URL to fetch SQL Data from Co-Op Postings: 
API_URL = "http://web-api:4000/system_diagnostics"

# Fetch coop postings from API
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    coop_postings_data = response.json()  # Get JSON data
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")
    coop_postings_data = []

# STYLING for Co-op listings
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

# Fetch coop postings from API
API_URL = "http://web-api:4000/system_diagnostics"
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    diagnostics = response.json()  # Get JSON data
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")
    diagnostics = []

# PAGE SETUP + HEADERS:
logger.info("Loading the Home page of PackTrack..")
st.write('\n\n')

st.markdown(f"""<h3 style="margin:0;"> System Diagnostics for PackTrack </h3>""", unsafe_allow_html=True)

# API fetch and iteration through coop postings
import streamlit as st
import requests

# Assuming diagnostics is defined
if diagnostics:
    try:
        response = requests.get(API_URL)
        if response.status_code == 200 and response != None:
            feedback = response.json()
            rows = len(feedback)
            
            # Prepare a list to hold each feedback item as a dictionary for table representation
            table_data = []
            
            for i in range(rows):
                d = feedback[i]
                
                appMetrics_id = d['appMetrics_id']
                status = d['status']
                metric = d['metric']
                errorCount = d['errorCount']
                responseTimeToFix = d['responseTimeToFix']
                coopPostSpeed = d['coopPostSpeed']

                table_data.append({
                    'App Metrics ID': appMetrics_id,
                    'Status': status,
                    'Metric': metric,
                    'Error Count': errorCount,
                    'Response Time to Fix': responseTimeToFix,
                    'Co-op Post Speed': coopPostSpeed
                })
            
            # Display the table with the collected data
            st.table(table_data)

        else: 
            # If the response status code is not 200, show an error
            st.write(f"Error Response Text: {feedbackresponse.status_code}")

    except ValueError as e:
        st.write("Error: Unable to decode JSON.")
        st.write("Response content:", feedbackresponse.text)


else:
    st.write("No system metrics available.")