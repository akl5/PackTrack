import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme,PublicPageNav

# Apply theme settings
Theme()
# Control the sidebar content
SideBarLinks(show_home=False)
#Public Page Navs 
st.session_state['authenticated'] = False
PublicPageNav()

# API endpoint URL to fetch SQL Data from Co-Op Postings: 
API_URL = "http://web-api:4000/coop_postings_by_latest_review"

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
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    coop_postings_data = response.json()  # Get JSON data
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")
    coop_postings_data = []

# PAGE SETUP + HEADERS:
logger.info("Loading the Home page of PackTrack..")
st.write('\n\n')

st.markdown(f"""<h3 style="margin:0;"> All Active Co-Op Listings </h3>""", unsafe_allow_html=True)

# API fetch and iteration through coop postings
if coop_postings_data:
    # Create a container for the columns (3 columns in each row)
    num_columns = 3
    num_rows = len(coop_postings_data) // num_columns + (1 if len(coop_postings_data) % num_columns else 0)

    # Loop over the rows
    for row_idx in range(num_rows):
        cols = st.columns(num_columns)
        
        # Loop over the columns in this row
        for col_idx, col in enumerate(cols):
            posting_idx = row_idx * num_columns + col_idx  # Calculate which posting we're at

            if posting_idx < len(coop_postings_data):
                posting = coop_postings_data[posting_idx]
                try:
                    jobTitle = posting.get('jobTitle', "Unknown Title")
                    companyName = posting.get('companyName', "Unknown Company")
                    location = posting.get('location', "Unknown Location")
                    jobType = posting.get('jobType', "Unknown Type")
                    lastUpdatedReviewDate = posting.get('lastUpdatedReviewDate', None)
                    jobDescription = posting.get('jobDescription', "No description available")
                    coopPosting_id = posting.get('coopPosting_id', "Unknown ID")

                except KeyError as e:
                    logger.error(f"Missing key: {e}")
                    continue  # Skip this posting if a key is missing

                # Handle NULL or missing review date
                review_date_display = (
                    f"Latest review: {lastUpdatedReviewDate}"
                    if lastUpdatedReviewDate
                    else "No reviews yet"
                )

                # Now, display this job info dynamically inside the correct column
                with col:
                    st.markdown(
                        f"""
                        <div style="
                            background-color: #DAEEFE; 
                            border-radius: 60px; 
                            padding: 10%; 
                            width: 20rem; 
                            height: 20rem; 
                            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                            display: flex; 
                            flex-direction: column; 
                            justify-content: center; 
                            text-align: left;
                            padding: 2rem;
                        ">
                            <div style="font-weight: 300; font-size: 25px; font-weight: light; text-decoration: underline; margin-bottom: 10px;">
                                {jobTitle}
                            </div>
                            <p style="font-size: 20px; margin:0; font-weight: medium;"> {companyName} </p>
                            <p style="color:#747EAC; margin:0">{location}</p>
                            <p style="font-size:15px;"> {jobDescription[:80]}...</p>
                            <p> <strong>{review_date_display}</strong></p>
                        </div>
                        """, unsafe_allow_html=True
                    )
                    # Button to navigate to full review (or any specific action)
                    st.write("\n")
                    col1, col2, col3 = st.columns([1, 4, 1])
                    with col2:
                        if st.button(f"View Full Review", key=f"view_{coopPosting_id}"):
                            st.session_state.co_op_posting_id = coopPosting_id
                            st.write(f"Redirecting to the full review of {jobTitle}...")
                            st.switch_page(f"pages/3b_Coop_Posting_Single.py")
                    st.markdown("---")
            else:
                # If there are fewer postings than columns, we leave the extra columns empty
                with col:
                    st.markdown("")
else:
    st.write("No coop postings available.")