import streamlit as st

from data import EXPERIENCE


def render_experience():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("💼 Experience")

    st.write(
        "My practical internship experience in agricultural engineering, "
        "farm machinery, tractor systems, testing, and soil and water conservation."
    )

    st.divider()


    # ==========================================
    # EXPERIENCE TIMELINE
    # ==========================================

    for index, experience in enumerate(EXPERIENCE):

        # Experience number
        st.markdown(
            f"""
            <p class="experience-number">
                EXPERIENCE {index + 1}
            </p>
            """,
            unsafe_allow_html=True
        )


        # ==========================================
        # EXPERIENCE CARD
        # ==========================================

        st.markdown(
            f"""
            <div class="experience-card">

                <h2>
                    {experience["job_title"]}
                </h2>

                <h3>
                    {experience["company"]}
                </h3>

                <p>
                    📍 {experience["location"]}
                </p>

                <p>
                    📅 {experience["duration"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        # ==========================================
        # RESPONSIBILITIES
        # ==========================================

        st.subheader(
            "Key Responsibilities"
        )


        for description in experience["description"]:

            st.write(
                f"• {description}"
            )


        # ==========================================
        # SEPARATOR
        # ==========================================

        if index < len(EXPERIENCE) - 1:

            st.divider()


    # ==========================================
    # INTERNSHIP SUMMARY
    # ==========================================

    st.divider()

    st.header(
        "📌 Internship Highlights"
    )


    col1, col2 = st.columns(2)


    # ==========================================
    # CFMTTI
    # ==========================================

    with col1:

        st.info(
            """
            ### 🚜 Farm Machinery & Tractor Technology

            **CFMTTI, Budni**

            - Tractor systems
            - Tractor testing
            - Farm machinery
            - Preventive maintenance
            - Performance evaluation
            - Technical documentation
            """
        )


    # ==========================================
    # ICAR-IISWC
    # ==========================================

    with col2:

        st.success(
            """
            ### 🌱 Soil & Water Conservation

            **ICAR-IISWC, Dehradun**

            - Soil conservation
            - Water conservation
            - Watershed management
            - Irrigation practices
            - Field surveys
            - Technical documentation
            """
        )


    # ==========================================
    # CAREER GOAL
    # ==========================================

    st.divider()

    st.header(
        "🎯 Professional Goal"
    )

    st.write(
        "I aim to build a career in agricultural machinery, "
        "tractor design and development, CAD engineering, "
        "product design, and agricultural mechanization, "
        "where I can apply my knowledge of agricultural engineering "
        "and engineering design tools to develop practical and innovative solutions."
    )