# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")
    st.session_state.coopPosting_id = 0


def AboutPageNav():
    st.sidebar.page_link("pages/1_About.py", label = "About PackTrack", icon="🧠")
    st.session_state.coopPosting_id = 0

def GithubRepoNav():
    st.sidebar.page_link("https://github.com/akl5/PackTrack", label = "See Github Source Repo", icon="⚙️")
    st.session_state.coopPosting_id = 0


#Function for font styling for all pages 
def Theme():  
    st.markdown(
    """
    <style>
    /* Importing the Parkinsans font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Park+Sans:wght@300..800&display=swap');

    /* Apply Parkinsans font to the entire app */
    body {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to all headers (h1, h2, h3, etc.) */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to all Streamlit widgets like buttons, sliders, etc. */
    .stButton, .stTextInput, .stTextArea, .stSelectbox, .stSlider, .stRadio, .stCheckbox, .stDateInput, .stNumberInput {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to labels, titles, and any other text */
    label, .stLabel, .stText, st.Title {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to sidebar elements, including page links and titles */
    .css-1d391kg, .css-1v0mbdj, .stSidebar .stSelectbox, .stSidebar .stTextInput, .stSidebar .stRadio, .stSidebar .stButton, .stSidebar .stCheckbox, .stSidebar .stNumberInput, .stSidebar .stTextArea, .stSidebar .stDateInput {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply specifically to the page links in the sidebar */
    .css-1d391kg a {
        font-family: 'Parkinsans', sans-serif;
        text-decoration: none;
    }

    </style>
    """,
    unsafe_allow_html=True
)
    
    st.markdown(
    """
    <style>
    /* Importing the Parkinsans font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Park+Sans:wght@300..800&display=swap');

    /* Apply Parkinsans font to the entire app */
    body {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to all headers (h1, h2, h3, etc.) */
    h1, h2, h3, h4, h5, h7, h8 {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to all Streamlit widgets like buttons, sliders, etc. */
    .stButton, .stTextInput, .stTextArea, .stSelectbox, .stSlider, .stRadio, .stCheckbox, .stDateInput, .stNumberInput {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to labels, titles, and any other text */
    label, .stLabel, .stText {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply to sidebar elements, including page links and titles */
    .css-1d391kg, .css-1v0mbdj, .stSidebar .stSelectbox, .stSidebar .stTextInput, .stSidebar .stRadio, .stSidebar .stButton, .stSidebar .stCheckbox, .stSidebar .stNumberInput, .stSidebar .stTextArea, .stSidebar .stDateInput {
        font-family: 'Parkinsans', sans-serif;
    }

    /* Apply specifically to the page links in the sidebar */
    .css-1d391kg a {
        font-family: 'Parkinsans', sans-serif;
        text-decoration: none;
    }

    </style>
    """,
    unsafe_allow_html=True
)

def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, 
    which was put in the streamlit session_state object when logging in.
    """

    # Add a logo to the sidebar always
    st.sidebar.image("assets/PackTrack_Logo.png", width=150)
    st.write('### PackTrack')

    # If there is no logged-in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    # Show the Home page link 
    HomeNav()

    # # Show the other page navigators depending on the users' role.
    # if st.session_state["authenticated"]:

    #     # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
    #     if st.session_state["role"] == "pol_strat_advisor":
    #         PolStratAdvHomeNav()
    #         WorldBankVizNav()
    #         MapDemoNav()

    #     # If the user role is usaid worker, show the Api Testing page
    #     if st.session_state["role"] == "usaid_worker":
    #         PredictionNav()
    #         ApiTestNav()
    #         ClassificationNav()

    #     # If the user is an administrator, give them access to the administrator pages
    #     if st.session_state["role"] == "administrator":
    #         AdminPageNav()

    # Always show the About and Github Repo pages at the bottom of the list of links
    Theme()
    AboutPageNav()
    GithubRepoNav()

    # Always show the logout button if there is a logged-in user
    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")