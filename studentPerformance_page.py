import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
# st.set_page_config(page_title="Dropout Prediction", page_icon=":tada", layout="wide")



# HEADER SECTION
st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="font-size:30px;color:white;">Student Success Predictor - Edu Track</p> 
                <p style="font-size:12px;color:white;">Designed by David Okoth.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# # Load the trained model
# model = joblib.load("student_performance_model.pkl")

# # Create a function to validate input values
# def validate_input(value):
#     if value < 0 or value > 100:
#         st.warning("Input value should be between 0 and 100.")
#         return False
#     return True

# # Create the web application using Streamlit
# def show_studentPerformance_page():

    # st.title("Student Performance Prediction")

    # # Create input widgets for user selection
    # gender = st.selectbox("Select Gender", ["Male", "Female"])
    # Nationality = st.selectbox("Select Nationality", [ "KW", "lebanon", "Egypt", "SaudiArabia", "USA", "Jordan", "venzuela", "Iran", "Tunis", "Morocco", "Syria", "Palestine", "Iraq", "Lybia"])
    # Performance_Index = st.number_input("Enter Performance Index", min_value=0, max_value=100, value=50)
    # Previous_Performance_Scores = st.number_input("Enter Previous Performance Scores", min_value=0, max_value=100, value=50)
    # StudentAbsenceDays = st.selectbox("Select Student Absence Days", ["Under-7", "Above-7"])

    # # Check if the inputs are valid
    # is_valid_performance = validate_input(Performance_Index)
    # is_valid_previous_performance = validate_input(Previous_Performance_Scores)


    # ok = st.button("Predict Student Future Performance")
    # if ok:
    #     is_valid_performance and is_valid_previous_performance
    #     # Convert gender and student absence days to numerical values using label encoding
    #     gender_encoded = 0 if gender == "Male" else 1
    #     student_absence_days_encoded = 0 if StudentAbsenceDays == "Under-7" else 1

    #     # Prepare the input data for prediction
    #     data = pd.DataFrame({
    #         "gender": [gender_encoded],
    #         "Nationality": [Nationality],
    #         "Performance_Index": [Performance_Index],
    #         "Previous_Performance_Scores": [Previous_Performance_Scores],
    #         "StudentAbsenceDays": [student_absence_days_encoded]
    #     })

    #     # Make the prediction using the trained model
    #     prediction = model.predict(data)

    #     # Display the prediction result
    #     st.subheader("Prediction Result")
    #     if prediction[0] == 0:
    #         st.write("The student is predicted to fail.")
    #     else:
    #         st.write("The student is predicted to pass.")

# Load the trained model
model = joblib.load("student_performance_model.pkl")

# Function to validate input values for Performance_Index and Previous_Performance_Scores
def validate_score_input(score):
    try:
        score = int(score)
        if score < 0 or score > 100:
            return False
        return True
    except ValueError:
        return False

# Function to predict future performance
def predict_performance(gender, nationality, previous_scores, absence_days):
    # Validate input values for Performance_Index and Previous_Performance_Scores
    if not validate_score_input(previous_scores):
        return "Invalid input forPrevious_Performance_Scores. Please enter a value between 0 and 100."

    # Encode categorical features
    gender_encoded = 0 if gender == "Male" else 1
    absence_days_encoded = 0 if absence_days == "Under-7" else 1

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        "gender": [gender_encoded],
        "Nationality": [nationality],
        # "Performance_Index": [int(performance_index)],
        "Previous_Performance_Scores": [int(previous_scores)],
        "StudentAbsenceDays": [absence_days_encoded]
    })

    # Make the prediction using the trained model
    prediction = model.predict(input_data)[0]
    result = "Pass" if prediction == 1 else "Fail"
    return f"The student is predicted to {result} in the future."

# Streamlit app
def show_studentPerformance_page():
    st.title("Student Performance Prediction")

    # Input fields for user to provide data
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    nationality = st.selectbox("Select Nationality", [ 4,"KW", "lebanon", "Egypt", "SaudiArabia", "USA", "Jordan", "venzuela", "Iran", "Tunis", "Morocco", "Syria", "Palestine", "Iraq", "Lybia"])
    # performance_index = st.text_input("Enter Performance Index (0-100)")
    previous_scores = st.text_input("Enter Previous Performance Scores (0-100)")
    absence_days = st.selectbox("Select Student Absence Days", ["Under-7", "Above-7"])

    # Button to trigger prediction
    if st.button("Predict"):
        if not all([gender, nationality, previous_scores, absence_days]):
            st.warning("Please fill in all the fields.")
        else:
            prediction_result = predict_performance(gender, nationality, previous_scores, absence_days)
            st.success(prediction_result)





    


