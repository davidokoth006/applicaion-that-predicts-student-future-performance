import streamlit as st

def show_contact_page():

    with st.container():
        st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="font-size:30px;color:white;">Contact Us</p> 
                
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("##")

    st.markdown(
            """
            <div style="text-align:center; margin-top:20px">
                <p style="color:white;">We would love to hear from you! If you have any questions, feedback, or suggestions, please don't hesitate to get in touch with us.</p> 
                
            </div>
            """,
            unsafe_allow_html=True
        )


    with st.container():
            st.write("---")
            left_column, middlecol, right_column = st.columns(3)
            with left_column:
                st.write(
                    """
                    **Contact Information**
                - **Email**: [support@studentssuccesspredictor.com](mailto:support@studentssuccesspredictor.com)
                - **Phone**: +254 123-4567

                """
                )

            with middlecol:
                      st.write(
                    """
            
                    **Office Address**
                    ```
                    StudentsSuccess Predictor
                    123 Marakaru-Kibabii
                    Bungoma, 1699-50200
                    Kenya
                    ```

                    """
                )

            with right_column:
                st.markdown("""
                            
                    <div> 
                        <p><b>Social Media</p>
                        <p> Connect with us on social media for the latest updates and educational resources:</p>
                        <i class="fas fa-band-aid"></i><a href="https://www.twitter.com/studentsuccess">Twitter</a></br>
                        <i class="fas fa-band-aid"></i><a href="https://www.instagram.com/studentsuccess">Instagram</a></br>
                        <i class="fas fa-band-aid"></i><a href="https://www.facebook.com/studentsuccesspredictor">Facebook</a>
                    </div>
                
                """, unsafe_allow_html=True
                            )

        # Adding a decorative separator
    st.markdown("---")

        # Feedback form
    st.subheader("Feedback Form")
    with st.form("feedback_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit_button = st.form_submit_button("Submit")

    if submit_button:
            # Here, you can implement the logic to send the feedback to your backend or store it in a database.
            # For this example, we'll just display a confirmation message to the user.
            st.success("Thank you for your feedback! We will get back to you soon.")

        # # Adding a decorative footer
        # st.markdown(
        #     """
        #     <div style="text-align:center;margin-top:30px;">
        #         <p style="font-size:12px;color:white;">&copy; 2023 StudentsSuccess Predictor. All rights reserved.</p>
        #         <p style="font-size:12px;color:white;">Designed with &#10084; by David Okoth.</p>
        #     </div>
        #     """,
        #     unsafe_allow_html=True
        # )

