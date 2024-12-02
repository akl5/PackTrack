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
def doAll():
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
                <div style="flex: 1; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);">
                    <h4 style="margin: 0;">Necessary Skills</h4>
                    <ul style="margin: 15px 0 0 20px; padding: 0; list-style: disc;">
                        <li>Proficiency in Python and JavaScript</li>
                        <li>Experience with React and Node.js</li>
                        <li>Knowledge of cloud platforms (AWS, Azure)</li>
                        <li>Strong problem-solving skills</li>
                        <li>Excellent teamwork and communication</li>
                    </ul>
                    <!-- Apply Now Button -->
                        <div style="text-align: center; margin-top: 20px;">
                        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" style="text-decoration: none; background-color: #003366; color: white;
                        padding: 12px 30px; border-radius: 8px; font-size: 16px; font-weight: bold;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        Apply Now
                        </a>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ----------- Data Below the Main Co-op Review ------------

    st.markdown("""
        <h2 style="text-align: center;">Reviews From Previous Placements</h2>
    """, unsafe_allow_html=True)

    import streamlit as st

    # Define the container HTML structure with custom styles
    st.markdown("""
        <style>
        /* Style for the container */
        .review-container {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            width: 90%;
            max-width: 1000px;
            margin: 50px auto;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        }

        /* Left section with the profile image and dates */
        .profile-info {
            display: flex;
            gap: 20px;
        }
        
        .profile-info img {
            border-radius: 50%;
            width: 80px;
            height: 80px;
            object-fit: cover;
        }

        .profile-info .dates {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Name, degree, company info section */
        .info-details {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Return offer status */
        .offer-status {
            background-color: #3E4B8B;
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            width: fit-content;
            margin-top: 10px;
        }

        /* Section for the brief review, skills, and challenges */
        .review-section {
            margin-top: 20px;
        }

        .review-section p {
            margin: 5px 0;
        }

        /* Skills and challenges list styling */
        .skills-challenges ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        </style>

        <div class="review-container">
            <!-- Profile and Dates -->
            <div class="profile-info">
                <img src="https://via.placeholder.com/80" alt="Profile Image">
                <div class="dates">
                    <p><strong>Last Updated:</strong> December 1, 2024</p>
                    <p><strong>Created:</strong> October 15, 2024</p>
                </div>
            </div>

            <!-- Info Details -->
            <div class="info-details">
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Degree:</strong> Computer Science</p>
                <p><strong>College Class:</strong> Class of 2025</p>
                <p><strong>Company:</strong> Tech Innovators Inc.</p>
                <p><strong>Position:</strong> Software Developer Intern</p>
            </div>

            <!-- Return Offer Status -->
            <div class="offer-status">
                <p>Return Offer: Yes</p>
            </div>

            <!-- Review, Skills, and Challenges -->
            <div class="review-section">
                <p><strong>Brief Review:</strong> Worked on scalable applications, participated in code reviews, and collaborated with a diverse team.</p>
                <div class="skills-challenges">
                    <p><strong>Skills Learned:</strong></p>
                    <ul>
                        <li>Python & JavaScript</li>
                        <li>React & Node.js</li>
                        <li>Cloud Platforms (AWS, Azure)</li>
                    </ul>
                    <p><strong>Challenges Faced:</strong></p>
                    <ul>
                        <li>Debugging complex multi-threaded applications</li>
                        <li>Learning to manage time effectively in a fast-paced environment</li>
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

doAll()
