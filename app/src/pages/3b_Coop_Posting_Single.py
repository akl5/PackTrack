import streamlit as st
import requests
from modules.nav import SideBarLinks, Theme, PublicPageNav

# Set the theme and sidebar
Theme()
SideBarLinks()
PublicPageNav()

# Set the URL for the API endpoint
COOP_POSTINGS_API_URL = "http://web-api:4000/coop_postings"
FEEDBACK_POSTS_API_URL = "http://web-api:4000/feedback_posts"
# Ensure 'coopPosting_id' exists in session state, otherwise initialize it with a default value (1 in this case)
if 'co_op_posting_id' not in st.session_state or not st.session_state.co_op_posting_id:
    st.session_state.coopPosting_id = 1  # Default to ID 1 (or any default ID you want)

st.session_state['authenticated'] = False
coopPosting_id = st.session_state['co_op_posting_id']  # Use the stored coopPosting_id

# Fetch and display data based on the coopPosting_id
if coopPosting_id and coopPosting_id != 0:
    with st.spinner(f"Fetching data for Co-op Posting ID {coopPosting_id}..."):
        try:
            # Send GET request to the API to get the co-op posting data
            response = requests.get(f"{COOP_POSTINGS_API_URL}/{coopPosting_id}")

            # Check if the response is successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response directly (without storing it in session_state)
                coop_data = response.json()

                # Extract relevant data from the API response
                company_id = coop_data['company_id']
                companyName = coop_data['companyName']
                companyIndustry = coop_data['companyIndustry']
                companySize = coop_data['companySize']
                companyHeadquarters = coop_data['companyHeadquarters']

                jobTitle = coop_data['jobTitle']
                jobDescription = coop_data['jobDescription']
                location = coop_data['location']
                jobType = coop_data['jobType']
                pay = coop_data['pay']
                companyBenefits = coop_data['companyBenefits']
                requirements = coop_data['requirements']
                preferredSkills = coop_data['preferredSkills']
                hiringManagerEmail = coop_data['hiringManagerEmail']
                startDate = coop_data['startDate']
                endDate = coop_data['endDate']
                linkToApply = coop_data['linkToApply']

                # Render the data in the Streamlit markdown
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
                                    <a href="{linkToApply}" style="text-decoration: none; background-color: #003366; color: white;
                                    padding: 12px 30px; border-radius: 8px; font-size: 16px; font-weight: bold;
                                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                                    Apply Now
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        except requests.exceptions.RequestException as e:
            # Catch network or connection-related errors
            st.write(f"### Error: {e}")

    #DISPLAYING THE REVIEWS
    st.markdown("""
        <h2 style="text-align: center;">Reviews From Previous Placements</h2>
    """, unsafe_allow_html=True)
    try:
        feedbackresponse = requests.get(f"{FEEDBACK_POSTS_API_URL}/{coopPosting_id}")
        if feedbackresponse.status_code == 200 and feedbackresponse != None:
            feedback = feedbackresponse.json()
            rows = len(feedback)
            for i in range(rows):
                    f = feedback[i]
                    firstName = f['firstName']
                    lastName = f['lastName']
                    graduationYear = f['graduationYear']

                    writtenReview = f['writtenReview']
                    skillsLearned = f['skillsLearned']
                    challenges = f['challenges']
                    returnOffer = f['returnOffer']

                    createdAT = f['createdAT']
                    updatedAT = f['updatedAT']  

                    st.markdown(f"""
                        <div style="background-color: white; padding: 20px; border-radius: 15px; width: 90%; max-width: 1000px; margin: 50px auto; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);">
                            <div style="display: flex; gap: 25px;">
                                <div style="width:20%; align:left;">
                                    <img src="https://via.placeholder.com/80" alt="Profile Image" style="border-radius: 50%; padding: 3px; width: 100%; object-fit: cover; margin: 5%;">
                                    <p style="color:#747EAC; font-size: 0.9rem;"> <strong> Created: </strong>{createdAT}</p>
                                    <p style="color:#747EAC;font-size: 0.9rem;"> <strong> Last Updated: </strong>{updatedAT}
                                </div>
                                <div style="width:80%;">
                                    <h3 style="margin-bottom:0;"> {firstName} {lastName} </h3>
                                    <h5> Class of {graduationYear} </h5>
                                    <p> <strong> Return Offer: </strong>{returnOffer}</p>
                                    <h6 style="margin-bottom:0;"> Review </h6> 
                                    <p> {writtenReview} </p>
                                    <p> <strong> Skills Learned: </strong>{skillsLearned}</p>
                                    <p> <strong> Challenges: </strong>{challenges}</p>
                                </div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            # REMOVE THIS BUTTON WHEN DONE DEBUGGING
            def writeButton():
                    # Center the button using columns
                    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column width for centering
                    with col2:
                        if st.button("Write a Review", key="write_review"):
                            st.write("Redirecting to the writing review page...")
                            st.switch_page("pages/4a_Writing_Review.py")  # Switch to the desired page

            writeButton()
        else: 
            # If the response status code is not 200, show an error
            st.write(f"Error Response Text: {feedback.status_code}")
    except ValueError as e:
        st.write("Error: Unable to decode JSON.")
        st.write("Response content:", feedback.text)
        

else:
    # If no data is available or coopPosting_id is invalid, show an error message
    st.write("### Error fetching data for current Co-Op Listing.")