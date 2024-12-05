import streamlit as st
import requests

# Set the URL for the API endpoint (adjust the base URL to match your app)
API_URL = "http://web-api:4000/coop_postings"

# Streamlit UI
st.title("Co-Op Posting Viewer")

# Assuming state_id is available and initialized (this would be the co-op posting ID)
if 'state_id' not in st.session_state:
    st.session_state.state_id = 1  # Replace this with your actual default or logic for state_id

# Use session state to store coopPosting_id and fetched data based on state_id
if 'coopPosting_id' not in st.session_state:
    st.session_state.coopPosting_id = st.session_state.state_id  # Initialize with state_id

coopPosting_id = st.session_state.coopPosting_id  # The co-op posting ID to fetch data for

# Fetch and display data based on the coopPosting_id
if coopPosting_id and coopPosting_id != 0:
    if 'coop_data' not in st.session_state or st.session_state.coop_data is None:
        # Fetch data from API only if it's not already fetched or ID has changed
        with st.spinner(f"Fetching data for Co-op Posting ID {coopPosting_id}..."):
            try:
                # Send GET request to the API to get the co-op posting data
                response = requests.get(f"{API_URL}/{coopPosting_id}")

                # If the response is successful (status code 200), save the data in session state
                if response.status_code == 200:
                    st.session_state.coop_data = response.json()  # Save the fetched data to session state
                else:
                    st.session_state.coop_data = None  # No data found, clear the previous data
                    st.error(f"Error: {response.json().get('error', 'Unknown error occurred')}")
            except requests.exceptions.RequestException as e:
                st.session_state.coop_data = None
                st.error(f"Error fetching data: {e}")
    
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
