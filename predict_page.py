# import streamlit as st
# import pickle
# import numpy as np

# def load_model():
#    with open('saved_steps.pkl', 'rb') as file:
#     data = pickle.load(file)
#     return data

# data = load_model()

# regressor = data["model"]
# le_hoursstudied = data["le_hoursstudied"]
# le_previousscores = data["le_previousscores"]
# le_sleephours = data["le_sleephours"]
# le_performanceindex = data["le_performanceindex"]  
# le_studentattendance = data["le_studentattendance"]

# def show_predict_page():
#     st.title("Predict Students Dropout Probability")
#     st.subheader("Enter Requested Info to Predict")

#     Hours_Studied = st.number_input("Enter hours you studied")
#     Previous_Scores = st.number_input("Enter Your Previous Exam mean Score")
#     Sleep_Hours = st.slider("Select Your Sleep Hours", 0, 20, 2)
#     Performance_Index = st.slider("Select Your Performance_Index", 0, 100, 0)
#     Students_Attendance = st.number_input("Input your attendance percentage")

#     # ok = st.button("Predict Dropout")
#     # if ok:
#     #    x = np.array([[Hours_Studied, Previous_Scores, Sleep_Hours, Performance_Index, Students_Attendance]])
#     #    x = x.astype(float)

#     #    dropout = regressor.predict(x)
#     #    st.success(f"Your Dropout Probability is {dropout[0]:.4}")

    
#     ok = st.button("Predict Dropout")
#     if ok:
#        x = np.array([[Hours_Studied, Previous_Scores, Sleep_Hours, Performance_Index, Students_Attendance]])
#        x = x.astype(float)

#        dropout = regressor.predict(x)
#        dropout_probability = dropout[0]

#        if dropout_probability <= 0.6600:
#            st.warning(f"Your Dropout Probability is {dropout_probability:.6}. You are at risk of dropping out.")
#        else:
#            st.success(f"Your Dropout Probability is {dropout_probability:.6}. You are likely to graduate.")




import streamlit as st
import numpy as np
import joblib

def load_model():
    # Load the model
    model = joblib.load('dropout_prediction_model.pkl')
    # Load the label encoder
    label_encoder = joblib.load('dropout_prediction_model_label_encoder.pkl')
    return model, label_encoder

model, label_encoder = load_model()

def show_predict_page():
    st.title("Predict Students Dropout Probability")
    st.subheader("Enter Requested Info to Predict")

    Hours_Studied = st.number_input("Enter hours you studied")
    Previous_Scores = st.number_input("Enter Your Previous Exam mean Score")
    Extracurricular_Activities = st.selectbox("Select Extracurricular Activities", ['Yes', 'No'])
    Sleep_Hours = st.slider("Select Your Sleep Hours", 0, 20, 2)
    Performance_Index = st.slider("Select Your Performance_Index", 0, 100, 0)
    Students_Attendance = st.number_input("Input your attendance percentage")

    ok = st.button("Predict Dropout")
    if ok:
        # Use the label encoder to transform the 'Extracurricular_Activities' input
        Extracurricular_Activities_encoded = label_encoder.transform([Extracurricular_Activities])[0]

        # Create the input array for prediction
        x = np.array([[Hours_Studied, Previous_Scores, Extracurricular_Activities_encoded, Sleep_Hours, Performance_Index, Students_Attendance]])
        x = x.astype(float)

        # Predict dropout probability
        dropout_probability = model.predict_proba(x)[:, 1][0]

        if dropout_probability <= 0.64:
            st.warning(f"Your Dropout Probability is {dropout_probability:.4}. You are at risk of dropping out.")
        else:
            st.success(f"Your Dropout Probability is {dropout_probability:.4}. You are likely to graduate.")




