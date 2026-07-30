import streamlit as st

from data import (
    ACHIEVEMENTS,
    CERTIFICATIONS,
    MEMBERSHIPS,
    LEADERSHIP
)


def render_achievements():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("🏆 Achievements & Activities")

    st.write(
        "My achievements, leadership experience, professional "
        "memberships, certifications, and extracurricular activities."
    )

    st.divider()


    # ==========================================
    # ACHIEVEMENTS
    # ==========================================

    st.header("🏆 Achievements")

    achievement_columns = st.columns(2)

    for index, achievement in enumerate(ACHIEVEMENTS):

        with achievement_columns[index % 2]:

            st.markdown(
                f"""
                <div class="section-card">

                    <h3>
                        {achievement["title"]}
                    </h3>

                    <p>
                        {achievement["description"]}
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    st.divider()


    # ==========================================
    # CERTIFICATIONS
    # ==========================================

    st.header("📜 Certifications")

    certification_columns = st.columns(2)

    for index, certification in enumerate(CERTIFICATIONS):

        with certification_columns[index % 2]:

            st.success(
                f"✓ {certification}"
            )


    st.divider()


    # ==========================================
    # LEADERSHIP
    # ==========================================

    st.header("👨‍💼 Leadership Experience")

    for role in LEADERSHIP:

        st.markdown(
            f"""
            <div class="section-card">

                <h3>
                    {role["title"]}
                </h3>

                <p>
                    <strong>
                        {role["organization"]}
                    </strong>
                </p>

                <p>
                    📅 {role["duration"]}
                </p>

                <p>
                    {role["description"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("**Key Responsibilities:**")

        for responsibility in role["responsibilities"]:

            st.write(
                f"• {responsibility}"
            )


    st.divider()


    # ==========================================
    # PROFESSIONAL MEMBERSHIP
    # ==========================================

    st.header("🤝 Professional Memberships")

    for membership in MEMBERSHIPS:

        st.markdown(
            f"""
            <div class="section-card">

                <h3>
                    {membership["organization"]}
                </h3>

                <p>
                    <strong>
                        Role:
                    </strong>
                    {membership["role"]}
                </p>

                <p>
                    <strong>
                        Duration:
                    </strong>
                    {membership["duration"]}
                </p>

                <p>
                    {membership["description"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()


    # ==========================================
    # EXTRACURRICULAR ACTIVITIES
    # ==========================================

    st.header("🎯 Extracurricular Activities")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
            ### 🏆 Sports

            Tug of War

            **1st Position**
            """
        )


    with col2:

        st.info(
            """
            ### 🤝 NSS

            Participated in NSS activities
            and community-oriented initiatives.
            """
        )


    with col3:

        st.info(
            """
            ### 🌱 CSAR

            Participated in CSAR activities
            as part of university engagement.
            """
        )


    # ==========================================
    # PROFESSIONAL DEVELOPMENT
    # ==========================================

    st.divider()

    st.header("🚀 Professional Development")

    st.write(
        "I continuously work on developing my technical and professional "
        "skills through internships, engineering projects, certifications, "
        "student activities, and leadership responsibilities."
    )