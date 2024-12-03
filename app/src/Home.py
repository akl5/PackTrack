import streamlit as st
import logging
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

# Control the sidebar content
SideBarLinks(show_home=False)

# The login button using Streamlit's native method (alternative method)
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

# # Define the login button to switch to another page
# def login_button():
#     # Create a button that acts as the "Login" button
#     if st.button("Test"):
#         # This will switch to the login page
#         st.page_link("2a_Coop_Posting.py") 

# The major content of this page
logger.info("Loading the Home page of PackTrack..")
st.write('\n\n')
st.markdown("""
<div style="display: flex; justify-content: flex-end; gap: 20px; padding-right: 20px; font-size: 20px;">
   <a href="/pages/CO_OP_Listings" style="text-decoration: none; color: #3E4B8B;">
       <h3>View CO-OP Listings</h3>
   </a>
   <a href="/pages/Latest_Reviews" style="text-decoration: none; color: #3E4B8B;">
       <h3>View Latest Reviews</h3>
   </a>
</div>
""", unsafe_allow_html=True)

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
    <!-- View More Link -->
    <a href="/show_more" style="color: #3E4B8B; text-decoration: underline; margin-top: 20px; display: inline-block; font-size: 28px;">View More</a>
</div>
""", unsafe_allow_html=True)

# End of the major content of the page