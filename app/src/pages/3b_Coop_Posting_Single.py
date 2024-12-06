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
        
        # Display the Co-op Posting Information
        st.write(f"### Co-op Posting Details for ID {coopPosting_id}")
        st.write("**Company ID**:", company_id)
        st.write("**Job Title**:", jobTitle)
        st.write("**Job Description**:", jobDescription)
        st.write("**Location**:", location)
        st.write("**Job Type**:", jobType)
        st.write("**Pay**:", pay)
        st.write("**Company Benefits**:", companyBenefits)
        st.write("**Hiring Manager Email**:", hiringManagerEmail)
        st.write("**Start Date**:", startDate)
        st.write("**End Date**:", endDate)

        st.markdown(f"""
                <div style="background-color: #DBEFFF; color: #3E4B8B; padding: 30px; border-radius: 15px; margin: 20px auto; width: 90%; max-width: 900px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                    <!-- Header Section -->
                    <div style="margin-bottom: 20px;">
                        <h1 style="margin: 0;">{jobTitle}</h1>
                        <h5 style="margin: 5px 0;">{companyName}</h5>
                        <h6 style="margin:0, font-weight:700;">{location}</h6>
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
                                <p style="margin:0;"><strong>Preferred Skills</strong></p>
                                <p style="font-weight:300"; text-align: justify;">
                                    {preferredSkills}
                                </p>
                                <h5>About the Company</h5>
                                <p style="font-weight:300", margin:0, text-align: justify;"><strong>Industry:</strong>{companyIndustry}</p>
                                <p style="font-weight:300", margin:0, text-align: justify;"><strong>Company Size:</strong>{companySize}</p>
                                <p style="font-weight:300", margin:0, text-align: justify;"><strong>Company Headquarters:</strong>{companyHeadquarters}</p>                                
                            </div>
                        <!-- Right Side: Job Information -->
                        <div style="flex: 1; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 0px rgba(0, 0, 0, 0);">
                            <h5> Information</h5>
                            <p style="margin: 0;"> <strong>Start Date:</strong> {startDate}</p> 
                            <p style="margin: 0;"> <strong>End Date:</strong> {endDate}</p> 
                            <p> <strong>Pay:</strong> ${pay}/hr</p> 
                            <h5>More Information</h5>
                            <p style="margin: 0;"> <strong> Contact: </strong> Hiring Manager <a href="mailto:{hiringManagerEmail}" target="_blank">{hiringManagerEmail}</a></p>
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

    else:
        # If no data is available, display an error message
        st.write("### Error fetching data for current Co-Op Listing.")