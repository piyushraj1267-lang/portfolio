import streamlit as st

from data import PERSONAL_INFO


def render_contact():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("📬 Contact Me")

    st.write(
        "I am open to internship opportunities, graduate engineer trainee "
        "roles, CAD/design engineering positions, agricultural machinery "
        "roles, and collaborations in agricultural technology."
    )

    st.divider()


    # ==========================================
    # CONTACT INFORMATION
    # ==========================================

    st.header("Let's Connect")

    col1, col2 = st.columns(2, gap="large")


    # ==========================================
    # CONTACT DETAILS
    # ==========================================

    with col1:

        st.markdown(
            f"""
            <div class="contact-card">

                <h3>📍 Location</h3>

                <p>
                    {PERSONAL_INFO["Bihar"]}
                </p>

                <h3>📧 Email</h3>

                <p>
                    {PERSONAL_INFO["piyushraj1267@gmail.com"]}
                </p>

                <h3>📞 Phone</h3>

                <p>
                    {PERSONAL_INFO["8235627969"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ==========================================
    # SOCIAL LINKS
    # ==========================================

    with col2:

        st.markdown(
            """
            <div class="contact-card">

                <h3>🌐 Professional Profiles</h3>

                <p>
                    Connect with me through my professional
                    and technical profiles.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.link_button(
            "🔗 LinkedIn Profile",
            PERSONAL_INFO["https://www.linkedin.com/in/piyush-raj-166b47235/"],
            use_container_width=True
        )

        st.link_button(
            "💻 GitHub Profile",
            PERSONAL_INFO["github"],
            use_container_width=True
        )


    st.divider()


    # ==========================================
    # CONTACT FORM
    # ==========================================

    st.header("✉️ Send Me a Message")

    st.write(
        "If you would like to connect with me, "
        "you can use the form below."
    )


    with st.form(
        key="contact_form"
    ):

        name = st.text_input(
            "Piyush raj"
        )

        email = st.text_input(
            "piyushraj1267@gmail.com"
        )

        subject = st.text_input(
            "Subject"
        )

        message = st.text_area(
            "Your Message",
            height=500
        )


        submitted = st.form_submit_button(
            "Send Message"
        )


        if submitted:

            if (
                name
                and email
                and subject
                and message
            ):

                st.success(
                    "Thank you for your message! "
                    "I will get back to you soon."
                )

            else:

                st.warning(
                    "Please fill in all the fields before submitting."
                )


    # ==========================================
    # CAREER OPPORTUNITIES
    # ==========================================

    st.divider()

    st.header(
        "🎯 Open to Opportunities"
    )

    col1, col2, col3 = st.columns(3)


    with col1:

        st.info(
            """
            ### 🚜 Agricultural Engineering

            Farm Machinery

            Tractor Systems

            Agricultural Mechanization
            """
        )


    with col2:

        st.info(
            """
            ### 💻 CAD & Design

            CATIA V5

            3DEXPERIENCE

            Product Design
            """
        )


    with col3:

        st.info(
            """
            ### 📊 Engineering Analysis

            ANSYS

            FEA

            Structural Analysis
            """
        )