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

def write_review_form():
    # Create a white container
    with st.container():
        st.title("Write a Review")  # Container title

        # Input boxes for each field
        name = st.text_input("Your Name")
        student_id = st.text_input("Student ID")
        employee_id = st.text_input("Student Employee ID")
        return_offer = st.radio("Return Offer (Yes or No)", ("Yes", "No"))
        skills_learned = st.text_area("Skills Learned")
        challenges = st.text_area("Challenges")
        written_review = st.text_area("Written Review")

        # Submit button
        if st.button("Submit"):
            # Display entered data for now (can be extended to save to a database)
            st.success("Your review has been submitted!")
            st.write("### Review Summary")
            st.write(f"**Name:** {name}")
            st.write(f"**Student ID:** {student_id}")
            st.write(f"**Student Employee ID:** {employee_id}")
            st.write(f"**Return Offer:** {return_offer}")
            st.write(f"**Skills Learned:** {skills_learned}")
            st.write(f"**Challenges:** {challenges}")
            st.write(f"**Written Review:** {written_review}")

# Display the review form
write_review_form()