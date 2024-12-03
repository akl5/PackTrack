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

st.write("## Welcome, Co-op Manager!")
st.write("### All Active Co-op Listings")

# Define a function to create a single horizontal container
def create_coop_container(coop_name, coop_id, company, created_time, num_applications):
    with st.container():
        st.markdown(
            f"""
            <div style="
                background-color: #DAEEFE;
                padding: 15px;
                margin-bottom: 10px;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            ">
                <div style="flex: 1; padding-right: 10px;">
                    <p><strong>Co-op Name:</strong> {coop_name}</p>
                    <p><strong>Co-op ID:</strong> {coop_id}</p>
                    <p><strong>Company:</strong> {company}</p>
                </div>
                <div style="flex: 1; padding-right: 10px;">
                    <p><strong>Created Time:</strong> {created_time}</p>
                    <p><strong>Number of Applications:</strong> {num_applications}</p>
                </div>
                <div style="flex-shrink: 0;">
                    <button style="
                        background-color: #3E4B8B;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    ">Contact Company</button>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Example data for the containers
data = [
    ("Software Engineer Intern", "COOP123", "Tech Innovators Inc.", "Dec 1, 2024", 42),
    ("Data Scientist Intern", "COOP124", "AI Solutions Ltd.", "Nov 29, 2024", 30),
    ("Web Developer Intern", "COOP125", "Creative Webworks", "Nov 27, 2024", 15),
    ("Product Manager Intern", "COOP126", "Future Enterprises", "Nov 25, 2024", 50),
]

st.title("Co-op Listings")

# Generate containers for each data entry
for entry in data:
    create_coop_container(*entry)
