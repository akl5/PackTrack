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
API_URL = "http://web-api:4000/coop_postings"

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
           text-align: center;  /* Left align the text */
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

if coop_postings_data:
    for posting in coop_postings_data:
        try:
            coopPosting_id = posting['coopPosting_id']  # Correct key from the API response
            jobTitle = posting['jobTitle']
            jobDescription = posting['jobDescription']
            location = posting['location']
            jobType = posting['jobType']
            pay = posting['pay']
            companyBenefits = posting['companyBenefits']
            startDate = posting['startDate']
            endDate = posting['endDate']
            linkToApply = posting['linkToApply']
            hiringManagerEmail = posting['hiringManagerEmail']
        except KeyError as e:
            logger.error(f"Missing key: {e}")
            continue  # Skip this posting if a key is missing
        
        # Display the data using Streamlit
        st.markdown(f"### Job Title: {jobTitle}")
        st.markdown(f"**Location:** {location}")
        st.markdown(f"**Job Type:** {jobType}")
        st.markdown(f"**Pay:** ${pay}")
        st.markdown(f"**Company Benefits:** {companyBenefits}")
        st.markdown(f"**Start Date:** {startDate}")
        st.markdown(f"**End Date:** {endDate}")
        st.markdown(f"**Hiring Manager Email:** {hiringManagerEmail}")
        st.markdown(f"**Job Description:** {jobDescription}")
        st.markdown(f"**Link to Apply:** {linkToApply}")
        st.markdown("---")
else:
    st.write("No coop postings available.")


# col1, col2, col3 = st.columns(3)



# # Content for the first container
# with col1:
#    st.markdown(f"""
#    <div class="styled-container" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
#        <div class="styled-header">
#            <h3>CO-OP Review</h3>
#        </div>
#        <p>This container is an Example CO-OP Review. Click anywhere inside to view the full review.</p>
#        <div class="number-of-reviews">
#            <h5> 3 Reviews </h5>
#        </div>
#    </div>
#    """, unsafe_allow_html=True)


# # Content for the second container
# with col2:
#    st.markdown(f"""
#    <div class="styled-container" onclick="window.location.href='/pages/00_Pol_Strat_Home.py';">
#        <div class="styled-header">
#            <h3>CO-OP Review</h3>
#        </div>
#        <p>This container is an Example CO-OP Review. Click anywhere inside to view the full review.</p>
#        <div class="number-of-reviews">
#            <h5> 3 Reviews </h5>
#        </div>
#    </div>
#    """, unsafe_allow_html=True)


# # Content for the third container
# with col3:
#    st.markdown(f"""
#    <div class="styled-container" onclick=switchPageToReview()>
#        <div class="styled-header">
#            <h3>CO-OP Review</h3>
#        </div>
#        <p>This container is an Example CO-OP Review. Click anywhere inside to view the full review.</p>
#        <div class="number-of-reviews">
#            <h5> 3 Reviews </h5>
#        </div>
#    </div>
#    """, unsafe_allow_html=True)