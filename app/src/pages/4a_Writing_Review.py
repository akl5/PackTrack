import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme,PublicPageNav
import logging

# Apply theme settings
Theme()
PublicPageNav()

# Control the sidebar content
SideBarLinks(show_home=False)

logger = logging.getLogger(__name__)

# Backend API endpoint
API_URL = "http://web-api:4000/write_review"

# Page Header
st.title("Submit a New Co-op Review")
st.markdown("Please fill out the form below to share your feedback on your co-op experience.")

# Form inputs
with st.form("new_feedback_form"):
    # st.subheader("Student Details")
    # studentEmployee_id = st.text_input("Student Employee ID", placeholder="Enter your employee ID")
    st.subheader("Co-op Posting Details")
    coopPosting_id = st.text_input("Co-op Posting ID", placeholder="Enter the co-op posting ID")
    st.subheader("Review Details")
    writtenReview = st.text_area("Written Review", placeholder="Describe your experience")
    skillsLearned = st.text_input("Skills Learned", placeholder="E.g., teamwork, problem-solving")
    challenges = st.text_input("Challenges Faced", placeholder="E.g., tight deadlines")
    roleSuggestions = st.text_area("Role Suggestions", placeholder="Suggestions for improving the role")
    st.subheader("Offer Details")
    returnOffer = st.radio("Did you receive a return offer?", options=["Yes", "No"])
    
    # Submit button
    submitted = st.form_submit_button("Submit Review")

    # Submit form data to the backend API
    if submitted:
        # Prepare the payload
        payload = {
            "student_id": 1,
            "studentEmployee_id": 1,
            "coopPosting_id": int(coopPosting_id),
            "writtenReview": writtenReview,
            "skillsLearned": skillsLearned,
            "challenges": challenges,
            "roleSuggestions": roleSuggestions,
            "returnOffer": returnOffer
        }
        
        try:
            # Make the POST request to the backend API
            response = requests.post(API_URL, json=payload)    
            # Check the response status
            if response.status_code == 201:
                st.success("Review submitted successfully!")
            elif response.status_code == 400:
                st.warning("Please ensure all required fields are filled out correctly.")
            else:
<<<<<<< HEAD
                st.error(f"An error occurred while submitting your review: {response.status_code}")
=======
                st.error(f"An error occurred while submitting your review:")
>>>>>>> d59ae9d (Pulling)
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred: {e}")
            st.error(f"An error occurred: {e}")



