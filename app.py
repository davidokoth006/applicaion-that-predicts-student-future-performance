import io
import streamlit as st
from PIL import Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import base64
st.set_page_config(page_title="Dropout Prediction", page_icon=":mortarboard-fill", layout="wide")
from streamlit_option_menu import option_menu
from predict_page import show_predict_page
from explore_page import show_explore_page
from home_page import show_home_page
from about_page import show_about_page
from contact import show_contact_page
from help import show_help_page
from studentPerformance_page import show_studentPerformance_page


# #---------USER AUTHENITICATION-------
# names= ["David Okoth", "Brian Shikanga"]
# usernames = ["dokoth", "bshikanga"]

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rd") as file:
#     hashed_passwords = pickle.load(file)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
#                                     "logins", "abcdef", cookie_expiry_days=30)


# name, authentication_status, username = authenticator.login("Login", "main")
# if authentication_status ==False:
#     st.error("Username or paswword incorrect")
# if authentication_status == None:
#     st.warning("Please enter yuour username and password")
# if authentication_status:



with st.sidebar:
    selected = option_menu(
        menu_title="DASHBOARD",
        options=["Home","Dropout_prediction", "Performance_Prediction", "Explore", "About", "Contact", "Help"],
        icons=["houses", "mortarboard-fill", "mortarboard","stars", "info-circle", "telephone", "question-circle"],
        menu_icon="dashboard",
        default_index=0,
        orientation="vertical",
    )

if selected == "Home":
    show_home_page()    
if selected == "Dropout_prediction":
    show_predict_page()
if selected == "Performance_Prediction":
    show_studentPerformance_page()
if selected == "Explore":
    show_explore_page()
if selected == "About":
    show_about_page()
if selected == "Contact":
    show_contact_page()
if selected == "Help":
    show_help_page()


    # Adding a decorative footer


st.markdown(
            """
            ---
            <div style="text-align:center; margin-bottom:20px">
                <p style="color:blue;">Student Success Predictor - Edu Track</p>
                <p style="font-size:12px;color:white;">&copy; 2023 StudentsSuccess Predictor. All rights reserved.</p>
                <p style="font-size:12px;color:white;">Designed with &#10084; by David Okoth.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


#--------HIDE STREAMLIT STYE-------

hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style,unsafe_allow_html=True)
