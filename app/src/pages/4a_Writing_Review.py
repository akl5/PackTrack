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

    # Retrieve coop_id from query parameters
    query_params = st.query_params()
    coop_id = query_params.get("coop_id", [None])[0]

    if not coop_id:
        st.error("No Co-op selected. Please return to the reviews page.")
        return

    # Create a white container
    with st.container():
        st.title(f"Write a Review for Co-op ID {coop_id}")

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
            # Validation
            if not all([name, student_id, employee_id, skills_learned, challenges, written_review]):
                st.error("Please fill out all fields before submitting.")
            else:
                # Display entered data for now (can be extended to save to a database)
                st.success(f"Review submitted for Co-op ID {coop_id}!")
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

# "We need to add a route here to have the review inserted into a specific posting" -Danny
