import streamlit as st
import logging
import requests
from modules.nav import SideBarLinks, Theme

# Set up basic logging infrastructure
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit configuration: wide layout minimizes sidebar
st.set_page_config(layout="wide")

# Trick to "collapse" the sidebar
placeholder = st.sidebar.empty()

# If a user is at this page, we assume they are not authenticated.
st.session_state['authenticated'] = False

# Apply theme settings
Theme()
SideBarLinks(show_home=False)

# LOG IN TO DIFFERENT USER TYPES 
if st.button("Log In"):
    st.switch_page("pages/2_Login.py")

# The rest of your content...
st.markdown("""
   <style>
       /* General style for all h3 headers */
       .styled-header h3 {
           font-size: 22px;  /* Font size for the header */
           font-weight: light;  /* Optional: make the header bold */
           text-decoration: underline; /* Underline the header */
       }


       /* Style for the containers with background color and rounded corners */
       .styled-container {
           background-color: #DAEEFE;  /* Background color */
           border-radius: 60px;  /* 60px rounded corners */
           padding: 10%;  /* Padding inside the container */
           width: 18rem;
           height: 18rem;  /* Ensure container height fits content */
           box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);  /* Optional: slight shadow for depth */
           display: flex;  /* Use flexbox to make sure content stays inside the container */
           justify-content: center;
           flex-direction: column;
           text-align: center;  /* Left align the text */
           padding-left: 2rem; /* Add padding to the left to align the text better */
           cursor: pointer;  /* Make the container appear clickable */
           
       }


       /* Style for the buttons (static buttons) inside the container */
       .styled-button {
           font-size: 14px;
           margin-top: 15px;  /* Add some space above the button */
           cursor: pointer;
       }
   </style>
""", unsafe_allow_html=True)


#PAGE SETUP + HEADERS:
logger.info("Loading the Home page of PackTrack..")
st.write('\n\n')

# VIEW CO-OP LISTINGS SECTION + VIEW LATEST REVIEWS SECTION

with st.container():
    # Create a vertical layout (rows) using single columns
    st.page_link("pages/3_Coop_Listings.py", label="[VIEW CO-OP LISTINGS]", icon = "👀")
    st.write("")  # Adds space between the rows
    st.page_link("pages/3_Coop_Listings.py", label="[VIEW LATEST REVIEWS]", icon = "💡")



# Fetch coop postings from API
API_URL = "http://web-api:4000/coop_postings"
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    coop_postings_data = response.json()  # Get JSON data
except requests.exceptions.RequestException as e:
    logger.error(f"Error fetching data: {e}")
    coop_postings_data = []

# PAGE SETUP + HEADERS:
logger.info("Loading the Home page of PackTrack..")
st.write('\n\n')

# API fetch and iteration through coop postings
if coop_postings_data:
    # Create a container for the columns (3 columns in each row)
    num_columns = 3
    num_rows = len(coop_postings_data) // num_columns + (1 if len(coop_postings_data) % num_columns else 0)

    # Loop over the rows
    for row_idx in range(num_rows):
        cols = st.columns(num_columns)
        
        # Loop over the columns in this row
        for col_idx, col in enumerate(cols):
            posting_idx = row_idx * num_columns + col_idx  # Calculate which posting we're at

            if posting_idx < len(coop_postings_data):
                posting = coop_postings_data[posting_idx]
                try:
                    coopPosting_id = posting['coopPosting_id']  # Correct key from the API response
                    jobTitle = posting['jobTitle']
                    jobDescription = posting['jobDescription']
                    location = posting['location']
                    jobType = posting['jobType']
                    pay = posting['pay']
                    companyBenefits = posting['companyBenefits']
                    startDate = posting['startDate']
                    endDate = posting['endDate']
                    linkToApply = posting['linkToApply']
                    hiringManagerEmail = posting['hiringManagerEmail']
                except KeyError as e:
                    logger.error(f"Missing key: {e}")
                    continue  # Skip this posting if a key is missing

                # Now, display this job info dynamically inside the correct column
                with col:
                    st.markdown(
                        f"""
                        <div style="
                            background-color: #DAEEFE; 
                            border-radius: 60px; 
                            padding: 10%; 
                            width: 18rem; 
                            height: 18rem; 
                            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                            display: flex; 
                            flex-direction: column; 
                            justify-content: center; 
                            text-align: left;
                        ">
                            <div style="font-size: 22px; font-weight: light; text-decoration: underline; margin-bottom: 10px;">
                                {jobTitle}
                            </div>
                            <p>{jobDescription[:100]}...</p>
                            <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                                {location} | {jobType}
                            </div>
                        </div>
                        """, unsafe_allow_html=True
                    )
                    # Button to navigate to full review (or any specific action)
                    if st.button(f"View Full Review", key=f"view_{coopPosting_id}"):
                        st.write(f"Redirecting to the full review of {jobTitle}...")
                        st.switch_page(f"pages/coop_postings/{coopPosting_id}")
            else:
                # If there are fewer postings than columns, we leave the extra columns empty
                with col:
                    st.markdown("")

else:
    st.write("No coop postings available.")


# Create the first row of 3 containers
col1, col2, col3 = st.columns(3)

# First row
with col1:
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #DAEEFE; 
                border-radius: 60px; 
                padding: 10%; 
                width: 18rem; 
                height: 18rem; 
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                display: flex; 
                flex-direction: column; 
                align-items: left; 
                justify-content: center; 
                text-align: left;
            ">
                <div style="
                    font-size: 22px; 
                    font-weight: light; 
                    text-decoration: underline; 
                    margin-bottom: 10px;
                ">
                    CO-OP Review
                </div>
                <p>This container is an Example CO-OP Review. Click the button to view the full review.</p>
                <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                    3 Reviews
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        # Button to navigate to full review (could use on_click for page navigation or other actions)
        if st.button("View Full Review", 1):
            st.write("Redirecting to the full review...")  # Placeholder action for the button
            # Optionally, you can use st.switch_page() for actual navigation:
            st.switch_page("pages/3a_Coop_Posting.py")

with col2:
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #DAEEFE; 
                border-radius: 60px; 
                padding: 10%; 
                width: 18rem; 
                height: 18rem; 
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                display: flex; 
                flex-direction: column; 
                align-items: left; 
                justify-content: center; 
                text-align: left;
            ">
                <div style="
                    font-size: 22px; 
                    font-weight: light; 
                    text-decoration: underline; 
                    margin-bottom: 10px;
                ">
                    CO-OP Review
                </div>
                <p>This container is an Example CO-OP Review. Click the button to view the full review.</p>
                <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                    3 Reviews
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        # Button to navigate to full review (could use on_click for page navigation or other actions)
        if st.button("View Full Review", 2):
            st.write("Redirecting to the full review...")  # Placeholder action for the button
            # Optionally, you can use st.switch_page() for actual navigation:
            st.switch_page("pages/3a_Coop_Posting.py")

with col3:
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #DAEEFE; 
                border-radius: 60px; 
                padding: 10%; 
                width: 18rem; 
                height: 18rem; 
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                display: flex; 
                flex-direction: column; 
                align-items: left; 
                justify-content: center; 
                text-align: left;
            ">
                <div style="
                    font-size: 22px; 
                    font-weight: light; 
                    text-decoration: underline; 
                    margin-bottom: 10px;
                ">
                    CO-OP Review
                </div>
                <p>This container is an Example CO-OP Review. Click the button to view the full review.</p>
                <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                    3 Reviews
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        # Button to navigate to full review (could use on_click for page navigation or other actions)
        if st.button("View Full Review", 3):
            st.write("Redirecting to the full review...")  # Placeholder action for the button
            # Optionally, you can use st.switch_page() for actual navigation:
            st.switch_page("pages/3a_Coop_Posting.py")

# Add space between the rows
st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)


# Create the second row of 3 containers
col4, col5, col6 = st.columns(3)

# Second row
with col4:
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #DAEEFE; 
                border-radius: 60px; 
                padding: 10%; 
                width: 18rem; 
                height: 18rem; 
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                justify-content: center; 
                text-align: center;
            ">
                <div style="
                    font-size: 22px; 
                    font-weight: light; 
                    text-decoration: underline; 
                    margin-bottom: 10px;
                ">
                    CO-OP Review
                </div>
                <p>This container is an Example CO-OP Review. Click the button to view the full review.</p>
                <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                    3 Reviews
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        # Button to navigate to full review (could use on_click for page navigation or other actions)
        if st.button("View Full Review", 4):
            st.write("Redirecting to the full review...")  # Placeholder action for the button
            # Optionally, you can use st.switch_page() for actual navigation:
            st.switch_page("pages/3a_Coop_Posting.py")

with col5:
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #DAEEFE; 
                border-radius: 60px; 
                padding: 10%; 
                width: 18rem; 
                height: 18rem; 
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                justify-content: center; 
                text-align: center;
            ">
                <div style="
                    font-size: 22px; 
                    font-weight: light; 
                    text-decoration: underline; 
                    margin-bottom: 10px;
                ">
                    CO-OP Review
                </div>
                <p>This container is an Example CO-OP Review. Click the button to view the full review.</p>
                <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                    3 Reviews
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        # Button to navigate to full review (could use on_click for page navigation or other actions)
        if st.button("View Full Review", 5):
            st.write("Redirecting to the full review...")  # Placeholder action for the button
            # Optionally, you can use st.switch_page() for actual navigation:
            st.switch_page("pages/3a_Coop_Posting.py")

with col6:
    with st.container():
        st.markdown(
            """
            <div style="
                background-color: #DAEEFE; 
                border-radius: 60px; 
                padding: 10%; 
                width: 18rem; 
                height: 18rem; 
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); 
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                justify-content: center; 
                text-align: center;
            ">
                <div style="
                    font-size: 22px; 
                    font-weight: light; 
                    text-decoration: underline; 
                    margin-bottom: 10px;
                ">
                    CO-OP Review
                </div>
                <p>This container is an Example CO-OP Review. Click the button to view the full review.</p>
                <div style="font-size: 14px; margin-top: 15px; color: #3E4B8B; font-weight: bold;">
                    3 Reviews
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("\n")
        # Button to navigate to full review (could use on_click for page navigation or other actions)
        if st.button("View Full Review", 6):
            st.write("Redirecting to the full review...")  # Placeholder action for the button
            # Optionally, you can use st.switch_page() for actual navigation:
            st.switch_page("pages/3a_Coop_Posting.py")

# Content for the entire blue background section
st.markdown("""
<div style="background-color: #DBEFFF; color: #3E4B8B; padding: 40px 0; margin-top: 25px; margin-bottom: 0px; text-align: center; width: 100vw; 
    position: relative; left: 50%; transform: translateX(-50%); height: 600px;">
    <h2>View Roles with Latest Reviews</h2>
    <p>Users Will Go Below</p>
    <div style="display: flex; justify-content: center; margin-top: 30px; gap: 20px; max-width: 80%; margin: 0 auto;">
        <!-- First Container -->
        <div style="background-color: white; color: #3E4B8B; border-radius: 20px; text-align: left; padding: 20px; width: 380px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); display: flex; align-items: center;">
            <!-- Circular Image -->
            <img src="https://via.placeholder.com/80" alt="John's Picture" style="border-radius: 50%; width: 120px; height: 120px; margin-right: 15px;">
            <!-- Text Content -->
            <div>
                <h3 style="margin: 0;">John Doe</h3>
                <p style="margin: 5px 0;">Degree: BS in Computer Science</p>
                <p style="margin: 5px 0;">CO-OP: Software Developer</p>
                <p style="margin: 5px 0;">Description: Worked on full-stack application development and database design.</p>
            </div>
        </div>
        <!-- Second Container -->
        <div style="background-color: white; color: #3E4B8B; border-radius: 20px; text-align: left; padding: 20px; width: 380px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); display: flex; align-items: center;">
            <!-- Circular Image -->
            <img src="https://via.placeholder.com/80" alt="Jane's Picture" style="border-radius: 50%; width: 120px; height: 120px; margin-right: 15px;">
            <!-- Text Content -->
            <div>
                <h3 style="margin: 0;">Jane Smith</h3>
                <p style="margin: 5px 0;">Degree: Masters in Data Science</p>
                <p style="margin: 5px 0;">CO-OP: Data Analyst</p>
                <p style="margin: 5px 0;">Description: Conducted data analysis and visualization to drive business decisions.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
if st.button("View More", 16):
    st.write("Redirecting to the full review...")  # Placeholder action for the button
    # Optionally, you can use st.switch_page() for actual navigation:
    st.switch_page("pages/3_Coop_Listings.py")

# End of the major content of the page


