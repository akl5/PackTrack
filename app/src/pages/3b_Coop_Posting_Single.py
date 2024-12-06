import streamlit as st
import requests
from modules.nav import SideBarLinks, Theme

Theme()
SideBarLinks()

# Set the URL for the API endpoint
API_URL = "http://web-api:4000/coop_postings"

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
        
        #VARIABLES TO STORE THE DATA FROM THIS CO OP LISTING: 
        company_id = data['company_id']
        companyName = data['companyName']   
        companyIndustry = data['companyIndustry']
        companySize = data['companySize']
        companyHeadquarters = data['companyHeadquarters']

        jobTitle = data['jobTitle']
        jobDescription = data['jobDescription']
        location = data['location']
        jobType = data['jobType']
        pay = data['pay']
        companyBenefits = data['companyBenefits']
        requirements = data['requirements']
        preferredSkills = data['preferredSkills']
        hiringManagerEmail = data['hiringManagerEmail']
        startDate = data['startDate']
        endDate = data['endDate']
        linkToApply = data['linkToApply']

        st.markdown(f"""
                <div style="background-color: #DBEFFF; color: #3E4B8B; padding: 30px; border-radius: 15px; margin: 20px auto; width: 100%; max-width: 90rem; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                    <!-- Header Section -->
                    <div style="margin-bottom: 20px;">
                        <h1 style="margin:0;">{jobTitle}</h1>
                        <h4 style="margin:0;">{companyName}</h4>
                        <h6 style="margin:0">{location}</h6>
                        <p style="margin:0, font-weight:400;"><strong>Role Type:</strong> {jobType}</p>
                    </div>
                    <!-- Description Section -->
                    <div style="display: flex; gap: 20px;">
                        <!-- Left Side: Descriptions -->
                            <div style="flex: 3;">
                                <h3> Position Overview </h3>
                                <p style="font-weight:300"; text-align: justify;">
                                    {jobDescription}
                                </p>
                                <h5> Eligibility </h5>
                                <p style="font-weight:300"; text-align: justify;">
                                    {requirements}
                                </p>
                                <h5> Preferred Skills </h5>
                                <p style="font-weight:300"; text-align: justify;">
                                    {preferredSkills}
                                </p>
                                <h5>About the Company</h5>
                                <p style="font-weight:300, margin:0, text-align: justify;"><strong>Industry:</strong></p>
                                <p>{companyIndustry}</p>
                                <p style="font-weight:300, margin:0, text-align: justify;"><strong>Company Size:</strong></p>
                                <p>{companySize}</p>
                                <p style="font-weight:300, margin:0, text-align: justify;"><strong>Company Headquarters:</strong></p>       
                                <p>{companyHeadquarters}</p>
                            </div>
                        <!-- Right Side: Job Information -->
                        <div style="flex: 1; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);">
                            <h5 style="margin: 0;"> Role Information</h5>
                            <p style="margin: 0;"> <strong>Start Date:</strong> {startDate}</p> 
                            <p style="margin: 0;"> <strong>End Date:</strong> {endDate}</p> 
                            <p> <strong>Pay:</strong> ${pay}/hr</p> 
                            <h5 style="margin: 0;"> Company Benefits</h5>
                            <p style="margin: 0;"> {companyBenefits}</p> 
                            <p style="margin: 0;"> <strong> Contact Hiring Manager: </strong><a href="mailto:{hiringManagerEmail}" target="_blank"> {hiringManagerEmail}</a></p>
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
        
        st.markdown("""
            <h2 style="text-align: center;">Reviews From Previous Placements</h2>
            """, unsafe_allow_html=True)

        st.markdown(
            """
            <div style="background-color: white; padding: 20px; border-radius: 15px; width: 90%; max-width: 1000px; margin: 50px auto; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);">
                <div style="display: flex; gap: 20px;">
                    <div style="width:20%;">
                        <img src="https://via.placeholder.com/80" alt="Profile Image" style="border-radius: 50%; width: 80px; height: 80px; object-fit: cover;">
                        <p> left side left side </p>
                    </div>
                    <div style="width:80%;">
                        <p> right side right side </p>
                    </div>
                </div>
                <p> Last Updated: </p> 
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        # If no data is available, display an error message
        st.write("### Error fetching data for current Co-Op Listing.")