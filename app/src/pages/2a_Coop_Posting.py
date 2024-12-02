import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks, Theme

def display_coop_page():
    st.markdown("""
    <div style="background-color: #DBEFFF; color: #3E4B8B; padding: 30px; border-radius: 15px; margin: 20px auto; width: 90%; max-width: 900px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
        <!-- Header Section -->
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0;">Co-op Role: Software Developer</h2>
            <p style="margin: 5px 0;"><strong>Company:</strong> Tech Innovators Inc.</p>
            <p style="margin: 5px 0;"><strong>Location:</strong> San Francisco, CA</p>
            <p style="margin: 5px 0;">
                <strong>Review:</strong> 
                <span style="color: gold;">&#9733;&#9733;&#9733;&#9733;&#9734;</span> (4/5 stars)
            </p>
        </div>
        <!-- Description Section -->
        <div style="display: flex; gap: 20px;">
            <!-- Left Side: Descriptions -->
            <div style="flex: 3;">
                <p style="margin: 10px 0;"><strong>Position Description:</strong></p>
                <p style="margin: 10px 0; text-align: justify;">
                    Worked on designing and implementing scalable web applications using modern frameworks and cloud infrastructure.
                    Participated in code reviews, debugging, and deploying applications. Collaborated with cross-functional teams
                    to deliver high-quality software.
                </p>
                <p style="margin: 10px 0;"><strong>Company Description:</strong></p>
                <p style="margin: 10px 0; text-align: justify;">
                    Tech Innovators Inc. is a leading provider of innovative software solutions. The company focuses on driving
                    technological advancements in cloud computing, artificial intelligence, and enterprise software.
                </p>
            </div>
            <!-- Right Side: Necessary Skills -->
            <div style="flex: 1; background-color: #ffffff; color: #3E4B8B; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);">
                <h4 style="margin: 0;">Necessary Skills</h4>
                <ul style="margin: 15px 0 0 20px; padding: 0; list-style: disc;">
                    <li>Proficiency in Python and JavaScript</li>
                    <li>Experience with React and Node.js</li>
                    <li>Knowledge of cloud platforms (AWS, Azure)</li>
                    <li>Strong problem-solving skills</li>
                    <li>Excellent teamwork and communication</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)