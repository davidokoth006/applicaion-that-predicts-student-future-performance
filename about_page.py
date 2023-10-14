import streamlit as st

def show_about_page():

    st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="font-size:30px;color:white;">About Us</p> 
                
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("##")
    

    col1, col2 = st.columns(2)
    col1.markdown(
        """
        <div>
            <p style=text-align:center;font-size:20px;>Our Mission</p>
            <p style=font-family: san-serif;>Our mission is to empower students, educators, and parents with data-driven tools and predictions that will foster better decision-making and ultimately lead to improved academic outcomes. We believe that every student has unique strengths and challenges, and by leveraging the power of data and technology, we can create personalized pathways to success.</p>
        </div>


        """, unsafe_allow_html=True
    )

    col2.markdown(
        """
        <div>
            <p style=text-align:center;font-size:20px;>Our Vision</p>
            <p>our vision is to revolutionize the educational landscape by empowering students, educators, and parents with data-driven insights and personalized predictions. We strive to create a seamless platform that optimizes the learning journey for every student, fostering a culture of success and enabling them to reach their full potential.</p>
        </div>


        """,  unsafe_allow_html=True
    )

    st.markdown("##")
    st.markdown("---")

    st.markdown(
        """
        <div style=text-align:center;>
            <p style=font-size:20px;>How It Works</p>
            <p>Our Student Success Predictor uses advanced machine learning algorithms to analyze various academic and non-academic factors that influence a student's performance. By inputting relevant data such as past grades, study habits, extracurricular activities, and more, our system can generate personalized predictions and recommendations.</p>
        </div>

        """, unsafe_allow_html=True
    )

    st.markdown("##")
    st.markdown("---")

    st.markdown(
        """
        <div style="background-image: url(images/marketplace-blog7.jpg);">
            <p>We value your feedback and suggestions. If you have any questions, concerns, or ideas for improvement, please don't hesitate to reach out to us.</p>
            
        </div>

        <div style=text-align:center;>
            <p><b>Feel free to contact us on:<b></P>
            <p><b>Email:<b> <i>contact@studentpredictor.com<i></P>
            <p><b>Phone:<b> <i>+254 123-4567<i></P>
            <p><b>Address:<b> <i>123 -Kibabii, Bungoma, Kenya, 1699-50200<i></P>
        </div>

        <div style="background-image: url(images/marketplace-blog7.jpg);">
            <p>Thank you for choosing our Student Success Predictor. Together, let's pave the way for a brighter and more successful future for all students!</p>
            
        </div>

        """, unsafe_allow_html=True
    )

