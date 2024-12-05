import streamlit as st
import requests

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
