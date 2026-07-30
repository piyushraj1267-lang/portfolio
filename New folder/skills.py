import streamlit as st

from data import SKILLS


def render_skills():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("🛠️ Technical Skills")

    st.write(
        "My technical skills and knowledge across CAD design, "
        "engineering simulation, agricultural engineering, "
        "programming, and emerging agricultural technologies."
    )

    st.divider()


    # ==========================================
    # SKILL CATEGORIES
    # ==========================================

    for category, skills in SKILLS.items():

        st.header(category)

        # Create 3 columns
        columns = st.columns(3)

        # Display each skill
        for index, skill in enumerate(skills):

            with columns[index % 3]:

                st.markdown(
                    f"""
                    <div class="skill-card">

                        <h4>
                            ✓ {skill}
                        </h4>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.write("")


    # ==========================================
    # SKILL SUMMARY
    # ==========================================

    st.divider()

    st.header("💡 My Technical Focus")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 🚜 Agricultural Engineering

            - Tractor Systems
            - Farm Machinery
            - Farm Mechanization
            - Primary and Secondary Tillage
            - Combine Harvester
            - Micro Irrigation
            """
        )

    with col2:

        st.markdown(
            """
            ### 💻 Engineering & Technology

            - CATIA V5
            - 3DEXPERIENCE
            - ANSYS Workbench
            - Finite Element Analysis
            - Python
            - Arduino & IoT
            """
        )


    # ==========================================
    # CAREER INTEREST
    # ==========================================

    st.divider()

    st.header("🎯 Career Interests")

    st.write(
        "I am interested in entry-level opportunities in "
        "agricultural machinery, tractor design and development, "
        "CAD modelling, product design, engineering simulation, "
        "farm mechanization, and precision agriculture."
    )