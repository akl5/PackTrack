import streamlit as st
import requests
from modules.nav import SideBarLinks, Theme

Theme()
SideBarLinks()

# Set the URL for the API endpoint
API_URL = "http://web-api:4000/coop_postings"

# Streamlit UI
st.title("Co-Op Posting Viewer")

# Ensure 'coopPosting_id' exists in session state, otherwise initialize it with a default value (1 in this case)
if 'coopPosting_id' not in st.session_state or not st.session_state.coopPosting_id:
    st.session_state.coopPosting_id = 1  # Default to ID 1 (or any default ID you want)

coopPosting_id = st.session_state.coopPosting_id  # Use the stored coopPosting_id

# Fetch and display data based on the coopPosting_id
if coopPosting_id and coopPosting_id != 0:
    if 'coop_data' not in st.session_state or st.session_state.coop_data is None:
        # Fetch data from API only if it's not already fetched or ID has changed
        with st.spinner(f"Fetching data for Co-op Posting ID {coopPosting_id}..."):
            try:
                # Send GET request to the API to get the co-op posting data
                response = requests.get(f"{API_URL}/{coopPosting_id}")

                # Check if the response is successful (status code 200)
                if response.status_code == 200:
                    try:
                        # Try to parse JSON response
                        st.session_state.coop_data = response.json()
                    except ValueError:
                        # If JSON parsing fails, print an error message
                        st.session_state.coop_data = None
                        st.markdown(f"### Error: Failed to parse JSON from the response. Invalid JSON format.")
                        st.markdown(f"**Response Text**: {response.text}")
                else:
                    # If the response status code is not 200
                    st.session_state.coop_data = None
                    st.markdown(f"### Error: API call failed with status code {response.status_code}.")
                    st.markdown(f"**Response Text**: {response.text}")

            except requests.exceptions.RequestException as e:
                # Catch network or connection-related errors
                st.session_state.coop_data = None
                st.markdown(f"### Error: Failed to fetch data due to a network issue.")
                st.markdown(f"**Error Message**: {e}")

    # Display fetched data if it's available
    if st.session_state.coop_data:
        data = st.session_state.coop_data
        
        # Display the Co-op Posting Information
        st.write(f"### Co-op Posting Details for ID {coopPosting_id}")
        st.write("**Company ID**:", data['company_id'])
        st.write("**Job Title**:", data['jobTitle'])
        st.write("**Job Description**:", data['jobDescription'])
        st.write("**Location**:", data['location'])
        st.write("**Job Type**:", data['jobType'])
        st.write("**Pay**:", data['pay'])
        st.write("**Company Benefits**:", data['companyBenefits'])
        st.write("**Hiring Manager Email**:", data['hiringManagerEmail'])
        st.write("**Start Date**:", data['startDate'])
        st.write("**End Date**:", data['endDate'])
    else:
        # If no data is available, display an error message
        st.write("### Error fetching data for current Co-Op Listing.")

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