import streamlit as st

def show_help_page():
    with st.container():
        st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="font-size:30px;color:white;">Get Help</p> 
                
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("##")

    st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="color:white;">Welcome to the Help section of StudentsSuccess Predictor. If you have any questions or need assistance, you've come to the right place!</p> 
                
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("##")
    st.markdown("---")
    st.markdown(
            """
            <div style="text-align:center;">
                <p style="font-size:20px;color:white;">Frequently Asked Questions</p>   
            </div>
            """, unsafe_allow_html=True
    )
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    col1.markdown(
            """

            <div style="border-style: solid;text-align:center;">
                <p style=""><b>1. How can I predict my academic success?<b></p>
                <p>To predict your academic success, click on the "Predict Success" tab, enter your details, and our advanced algorithms will analyze the data to provide insights into your performance.</p>  
            </div>
            """, unsafe_allow_html=True
    )
    
    
    col2.markdown(
        """
         <div style="border-style: solid;text-align:center;">
                <p style=""><b>2. How do I interpret the predictions?<b></p>
                <p>Our predictions are based on historical data and are meant to be used as guidance. Higher predicted scores indicate a higher likelihood of success in a particular subject.</p>  
            </div>
        """,unsafe_allow_html=True
        )
    
    st.markdown("---")
    st.markdown("##")
    
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        <div style="border-style: solid;text-align:center;">
                <p style=""><b>3. How can educators and parents benefit from the Student Success Predictor?<b></p>
                <p>Educators and parents can access comprehensive reports and insights about each student's progress, strengths, and challenges. This information empowers them to tailor their teaching and support strategies to maximize each student's potential.</p>  
            </div>
        """,unsafe_allow_html=True
        )
    
    col2.markdown(
        """
        <div style="border-style: solid;text-align:center;">
                <p style=""><b>4. Is my data secure on the platform?<b></p>
                <p>Absolutely! We take data privacy and security seriously. Our platform employs robust encryption and follows industry best practices to safeguard all user data. Your information is kept confidential and will never be shared with third parties without your consent.</p>  
            </div>
        """,unsafe_allow_html=True
        )
    
    st.markdown("---")
    st.markdown("##")
    
    col1, col2 = st.columns(2)
    col1.markdown(
        """
        <div style="border-style: solid;text-align:center;">
                <p style=""><b>5. What data is required to use the Student Success Predictor?<b></p>
                <p>To generate accurate predictions, the platform requires various data points, including academic performance, study habits, extracurricular involvement, and personal interests. The more comprehensive and up-to-date the data, the more precise the predictions will be
                </p>  
            </div>
        """,unsafe_allow_html=True
        )
    
    col2.markdown(
        """
         <div style="border-style: solid;text-align:center;">
                <p style=""><b>6. What is the Student Success Predictor Web App?<b></p>
                <p>The Student Success Predictor Web App is an advanced educational platform that utilizes machine learning algorithms to provide personalized predictions and recommendations for students. It helps identify individual strengths, challenges, and learning patterns, enabling educators and parents to support students effectively.</p>  
            </div>
        """,unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("##")
    st.markdown("""
                <div style="border-style: solid;text-align:center;">
                <p style=""><b>7. How can I contact support if I have additional questions or encounter issues?<b></p>
                <p>For any questions, concerns, or technical support, please reach out to our dedicated support team through the "Contact Us" section on the website or by emailing <i>support@studentpredictor.com.<i></p>  
            </div>
                """, unsafe_allow_html=True)

           

            

            

            

           

            


    # st.write(
    #     """
       

    #     ****
    #     We've compiled a list of common questions and their answers to provide you with quick solutions.

    #     1. **How can I predict my academic success?**
    #     T

    #     2. **How do I interpret the predictions?**
    #     

    #     3. **How do I track my progress?**
    #     You can monitor your progress on the "Track Progress" tab, where you'll find visualizations and statistics showing your performance over time.

    #     **Contact Support**
    #     If you have specific questions, issues, or need personalized assistance, feel free to reach out to our support team.

    #     - **Email**: [support@studentssuccesspredictor.com](mailto:support@studentssuccesspredictor.com)
    #     - **Phone**: +1 (123) 456-7890

    #     **Feedback**
    #     Your feedback is invaluable to us. If you have any suggestions to improve the app or want to report a bug, use the feedback form on the "Contact Us" page.

    #     **Resources**
    #     Visit our "Resources" section for educational articles, tips, and guides to enhance your academic journey.

    #     """
    # )



                  