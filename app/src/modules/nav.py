# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/1_About.py", label = "About PackTrack", icon="🧠")

def GithubRepoNav():
    st.sidebar.page_link("https://github.com/akl5/PackTrack", label = "See Github Source Repo", icon="⚙️")


#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link(
        "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
    )


def WorldBankVizNav():
    st.sidebar.page_link(
        "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
    )


def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
    )

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
    h1, h2, h3, h4, h5, h6 {
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

    # Show the Home page link (the landing page) only if show_home is True
    if show_home:
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state["role"] == "pol_strat_advisor":
            PolStratAdvHomeNav()
            WorldBankVizNav()
            MapDemoNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "usaid_worker":
            PredictionNav()
            ApiTestNav()
            ClassificationNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()

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

# def SideBarLinks(show_home=False):
#     """
#     This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
#     """

#     # Add a logo to the sidebar always
#     st.sidebar.image("assets/PackTrack_Logo.png", width=150)
#     st.write('### PackTrack')

#     # If there is no logged-in user, redirect to the Home (Landing) page
#     if "authenticated" not in st.session_state:
#         st.session_state.authenticated = False
#         st.switch_page("Home.py")

#     # Show the Home page link (the landing page) only if show_home is True
#     if show_home:
#         HomeNav()

#     # Show the other page navigators depending on the users' role.
#     if st.session_state["authenticated"]:

#         # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
#         if st.session_state["role"] == "pol_strat_advisor":
#             PolStratAdvHomeNav()
#             WorldBankVizNav()
#             MapDemoNav()

#         # If the user role is usaid worker, show the Api Testing page
#         if st.session_state["role"] == "usaid_worker":
#             PredictionNav()
#             ApiTestNav()
#             ClassificationNav()

#         # If the user is an administrator, give them access to the administrator pages
#         if st.session_state["role"] == "administrator":
#             AdminPageNav()

#     # Always show the About and Github Repo pages at the bottom of the list of links
#     Theme()
#     AboutPageNav()
#     GithubRepoNav()

#     if st.session_state["authenticated"]:
#         # Always show a logout button if there is a logged-in user
#         if st.sidebar.button("Logout"):
#             del st.session_state["role"]
#             del st.session_state["authenticated"]
#             st.switch_page("Home.py")




# # --------------------------------Links Function -----------------------------------------------
# def SideBarLinks(show_home=False):
#     """
#     This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
#     """

#     # add a logo to the sidebar always
#     st.sidebar.image("assets/PackTrack_Logo.png", width=150)
#     st.write('### PackTrack')


#     # If there is no logged in user, redirect to the Home (Landing) page
#     if "authenticated" not in st.session_state:
#         st.session_state.authenticated = False
#         st.switch_page("Home.py")

#     # if show_home:
#     #     # Show the Home page link (the landing page)
#     #     HomeNav()

#     # Show the other page navigators depending on the users' role.
#     if st.session_state["authenticated"]:

#         # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
#         if st.session_state["role"] == "pol_strat_advisor":
#             PolStratAdvHomeNav()
#             WorldBankVizNav()
#             MapDemoNav()

#         # If the user role is usaid worker, show the Api Testing page
#         if st.session_state["role"] == "usaid_worker":
#             PredictionNav()
#             ApiTestNav()
#             ClassificationNav()

#         # If the user is an administrator, give them access to the administrator pages
#         if st.session_state["role"] == "administrator":
#             AdminPageNav()

#     # Always show the Home, About, and Github Repo page at the bottom of the list of links
#     Theme()
#     HomeNav()
#     AboutPageNav()
#     GithubRepoNav()

#     if st.session_state["authenticated"]:
#         # Always show a logout button if there is a logged in user
#         if st.sidebar.button("Logout"):
#             del st.session_state["role"]
#             del st.session_state["authenticated"]
#             st.switch_page("Home.py")