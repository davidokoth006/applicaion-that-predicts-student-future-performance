import streamlit as st
# st.set_page_config(page_title="Dropout Prediction", page_icon=":tada", layout="wide")

def show_home_page():

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


    with st.container():
        st.markdown("##")
        st.subheader("Forecasting Dropout Probability and Academic Performance")
        st.write("StudentSuccess Predictor is an innovative web application designed to empower educational institutions and educators with advanced predictive analytics. Leveraging cutting-edge machine learning algorithms and comprehensive student data, this platform accurately forecasts students dropout probability and academic performance.")
        st.write("[Learn more>](https://edutrack.free.nf/)")


    # SERVICES
    st.markdown("---")
    st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="font-size:30px;color:white;">What We Offer</p> 
            </div>
            """,
            unsafe_allow_html=True
        )



    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("images/stephen-dawson-qwtCeJ5cLYs-unsplash.jpg", width=400)

        with right_column:
            st.subheader("Dropout Probability Prediction")
            st.write("The app calculates the likelihood of a student dropping out based on historical data and current performance, flagging those who need extra attention and support.")


    with st.container():
        st.write("---")

        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Data Visualization and Reports")
            st.write("The app offers intuitive visualizations and detailed reports to present data in a user-friendly manner, enabling educators and administrators to make data-driven decisions effectively.")

        with right_column:
            st.image("images/lukas-blazek-mcSDtbWXUZU-unsplash.jpg", width=400)


    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.image("images/luke-chesser-JKUTrJ4vK00-unsplash.jpg", width=400)

        with right_column:
            st.subheader("Intervention Recommendations")
            st.write("The app generates personalized intervention strategies to help students overcome challenges, improve their academic performance, and stay on track to success.")


    st.markdown("##") 
    st.markdown("---")
    st.markdown(
        """
        <div style=text-align:center>
            <p>StudentSuccess Predictor aims to revolutionize the educational landscape by fostering a proactive approach to student support. By accurately identifying students at risk of dropping out and providing targeted interventions, educational institutions can create a more inclusive, supportive, and successful learning environment for all students.</p>
        </div>
        """,
        unsafe_allow_html=True

    )
    