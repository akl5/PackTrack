import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme
import time

# Apply theme settings
Theme()

# Control the sidebar content
SideBarLinks(show_home=False)

# URL endpoint
API_URL = "http://web-api:4000/coop_postings/company/1"
DELETE_URL = "http://web-api:4000/delete_coop_posting/"

# Fetch coop postings from API
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    coop_postings_data = response.json()  # Get JSON data
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")
    coop_postings_data = []

# Delete function
def delete_coop_posting(coopPosting_id):
    """Call the backend API to delete a co-op posting."""
    try:
        response = requests.delete(f"{DELETE_URL}{coopPosting_id}")
        if response.status_code == 200:
            # st.success(f"Successfully deleted co-op posting with ID {coopPosting_id}.")
            time.sleep(0.1)
            st.rerun()
        elif response.status_code == 404:
            st.warning(f"Co-op posting with ID {coopPosting_id} not found.")
        else:
            st.error("Failed to delete co-op posting.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

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
            company_id = posting['company_id']
            coopPosting_id = posting['coopPosting_id']  
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
            st.write(f"Error: {e}")
            continue  # Skip this posting if a there's an error with this entry 

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

        # Add Delete button
        if st.button(f"Delete {posting.get('jobTitle')}", key=f"delete-{coopPosting_id}"):
            response = delete_coop_posting(coopPosting_id)  # Call the delete function
            if response.status_code == 200:
                # st.success(f"Successfully deleted co-op posting with ID {coopPosting_id}.")
                time.sleep(500)
                st.experimental_rerun()  # Refresh the page after deletion
                # st.rerun()  # Refresh the page to show updated data
            elif response.status_code == 404:
                st.warning(f"Co-op posting with ID {coopPosting_id} not found.")
            else:
                st.error("Failed to delete co-op posting.")
        
        st.markdown("---")
else:
    st.write("No coop postings available.")
