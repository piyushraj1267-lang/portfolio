import streamlit as st

from data import (
    PERSONAL_INFO,
    EDUCATION,
    LEADERSHIP,
    MEMBERSHIPS,
    LANGUAGES,
    AREAS_OF_INTEREST
)


def render_about():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("👨‍🎓 About Me")

    st.write(
        "Get to know more about my education, leadership experience, "
        "professional memberships, and career interests."
    )

    st.divider()


    # ==========================================
    # ABOUT ME
    # ==========================================

    st.header("About Me")

    st.markdown(
        f"""
        <div class="section-card">

        <h3>{PERSONAL_INFO["name"]}</h3>

        <p>
        {PERSONAL_INFO["summary"]}
        </p>

        <p>
        I am currently pursuing a 
        <strong>{EDUCATION["degree"]}</strong> at 
        <strong>{EDUCATION["university"]}</strong>, 
        Odisha.
        </p>

        <p>
        My primary areas of interest include agricultural machinery,
        tractor design, CAD modelling, engineering simulation,
        farm mechanization, precision agriculture, and agricultural
        drone technology.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ==========================================
    # EDUCATION
    # ==========================================

    st.header("🎓 Education")

    col1, col2 = st.columns(
        [3, 1],
        gap="large"
    )

    with col1:

        st.subheader(
            EDUCATION["degree"]
        )

        st.write(
            f"🏫 {EDUCATION['university']}"
        )

        st.write(
            f"📍 {EDUCATION['location']}"
        )

    with col2:

        st.metric(
            "Status",
            EDUCATION["status"]
        )

        st.write(
            f"Graduation: {EDUCATION['graduation']}"
        )

        st.write(
            f"CGPA: {EDUCATION['cgpa']}"
        )


    st.divider()


    # ==========================================
    # LEADERSHIP EXPERIENCE
    # ==========================================

    st.header(
        "👨‍💼 Leadership & Positions of Responsibility"
    )


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


        st.write(
            "**Key Responsibilities:**"
        )


        for responsibility in role["responsibilities"]:

            st.write(
                f"• {responsibility}"
            )


    # ==========================================
    # PROFESSIONAL MEMBERSHIPS
    # ==========================================

    st.header(
        "🤝 Professional Memberships"
    )


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


    # ==========================================
    # AREAS OF INTEREST
    # ==========================================

    st.header(
        "🎯 Areas of Interest"
    )


    columns = st.columns(3)


    for index, interest in enumerate(
        AREAS_OF_INTEREST
    ):

        with columns[
            index % 3
        ]:

            st.info(
                interest
            )


    # ==========================================
    # LANGUAGES
    # ==========================================

    st.header(
        "🌐 Languages"
    )


    language_columns = st.columns(
        len(LANGUAGES)
    )


    for index, language in enumerate(
        LANGUAGES
    ):

        with language_columns[index]:

            st.success(
                language
            )