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

# Center the buttons and style them
col1, col2, col3 = st.columns([1, 1, 1])  # Center the buttons by using empty columns on the sides

with col1:  # Centered column for the buttons
    button_style = """
        <style>
            div.stButton > button {
                background-color: #3E4B8B;  /* Dark blue */
                color: white;  /* White text */
                padding: 15px 30px;  /* Increase padding for larger buttons */
                font-size: 18px;  /* Larger font size */
                border: none;  /* Remove borders */
                border-radius: 10px;  /* Rounded corners */
                width: 100%;  /* Full width of container */
                cursor: pointer;  /* Pointer cursor on hover */
            }
            div.stButton > button:hover {
                background-color: #2C3A6B;  /* Slightly darker blue on hover */
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)  # Apply the style
    
    if st.button("View All Active Co-op Listings"):
        st.switch_page("pages/8_All_Active_Listings.py")

with col2: 
    button_style = """
        <style>
            div.stButton > button {
                background-color: #3E4B8B;  /* Dark blue */
                color: white;  /* White text */
                padding: 15px 30px;  /* Increase padding for larger buttons */
                font-size: 18px;  /* Larger font size */
                border: none;  /* Remove borders */
                border-radius: 10px;  /* Rounded corners */
                width: 100%;  /* Full width of container */
                cursor: pointer;  /* Pointer cursor on hover */
            }
            div.stButton > button:hover {
                background-color: #2C3A6B;  /* Slightly darker blue on hover */
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)  # Apply the style
    
    if st.button("View All Listings By Date"):
        st.switch_page("pages/9_Listings_By_Date.py")