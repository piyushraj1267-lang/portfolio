import streamlit as st
from pathlib import Path

from data import PERSONAL_INFO


def render_hero():

    # ==========================================
    # HERO TITLE
    # ==========================================

    st.markdown(
        """
        <div class="hero">

            <p class="hero-label">
                AGRICULTURAL ENGINEERING PORTFOLIO
            </p>

            <h1>
                Piyush Raj
            </h1>

            <h2>
                Final-Year B.Tech Agricultural Engineering Student
            </h2>

            <p class="hero-headline">
                CAD/CAE | CATIA V5 | 3DEXPERIENCE | ANSYS |
                Farm Machinery | Agricultural Technology
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ==========================================
    # PROFILE IMAGE + INTRODUCTION
    # ==========================================

    col1, col2 = st.columns(
        [1, 2],
        gap="large"
    )


    # ==========================================
    # PROFILE IMAGE
    # ==========================================

    with col1:

        image_path = Path(
            PERSONAL_INFO["profile_image"]
        )

        if image_path.exists():

            st.image(
                str(image_path),
                width=300
            )

        else:

            st.info(
                "Please add your profile photo at: assets/profile.png"
            )


    # ==========================================
    # INTRODUCTION
    # ==========================================

    with col2:

        st.markdown(
            f"""
            <div class="intro-card">

                <h2>
                    Hello, I'm {PERSONAL_INFO["name"]} 👋
                </h2>

                <p>
                    {PERSONAL_INFO["summary"]}
                </p>

                <p>
                    📍 {PERSONAL_INFO["location"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


        # ==========================================
        # SOCIAL LINKS
        # ==========================================

        col_a, col_b, col_c = st.columns(3)


        with col_a:

            st.link_button(
                "LinkedIn",
                PERSONAL_INFO["linkedin"]
            )


        with col_b:

            st.link_button(
                "GitHub",
                PERSONAL_INFO["github"]
            )


        with col_c:

            st.link_button(
                "Email",
                f"mailto:{PERSONAL_INFO['email']}"
            )


        # ==========================================
        # RESUME DOWNLOAD
        # ==========================================

        resume_path = Path(
            PERSONAL_INFO["resume"]
        )


        if resume_path.exists():

            with open(
                resume_path,
                "rb"
            ) as resume:

                st.download_button(

                    "📄 Download Resume",

                    resume,

                    file_name="Piyush_Raj_Resume.pdf",

                    mime="application/pdf",

                    use_container_width=True

                )

        else:

            st.warning(
                "Please add your resume at: assets/resume.pdf"
            )


    # ==========================================
    # CORE INTERESTS
    # ==========================================

    st.divider()


    st.header(
        "🚜 My Core Interests"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.info(
            "🚜 Farm Machinery"
        )


    with col2:

        st.info(
            "💻 CAD / CAE"
        )


    with col3:

        st.info(
            "🚁 Agricultural Drones"
        )


    with col4:

        st.info(
            "🌱 Smart Agriculture"
        )