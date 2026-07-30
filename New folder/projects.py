import streamlit as st

from data import PROJECTS


def render_projects():

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.title("🚀 Projects")

    st.write(
        "A collection of my academic and technical projects "
        "in CAD design, engineering simulation, agricultural "
        "machinery, IoT, and precision agriculture."
    )

    st.divider()


    # ==========================================
    # PROJECT CARDS
    # ==========================================

    for index, project in enumerate(PROJECTS):

        # --------------------------------------
        # PROJECT NUMBER
        # --------------------------------------

        st.markdown(
            f"""
            <p class="experience-number">
                PROJECT {index + 1}
            </p>
            """,
            unsafe_allow_html=True
        )


        # --------------------------------------
        # PROJECT TITLE & CATEGORY
        # --------------------------------------

        st.markdown(
            f"""
            <div class="section-card">

                <h2>
                    {project["title"]}
                </h2>

                <p>
                    <strong>
                        Category:
                    </strong>
                    {project["category"]}
                </p>

                <p>
                    {project["description"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        # --------------------------------------
        # PROJECT COMPONENTS
        # --------------------------------------

        st.subheader(
            "Key Components / Work"
        )


        component_columns = st.columns(3)


        for component_index, component in enumerate(
            project["components"]
        ):

            with component_columns[
                component_index % 3
            ]:

                st.info(
                    component
                )


        # --------------------------------------
        # TECHNOLOGIES USED
        # --------------------------------------

        st.subheader(
            "Technologies & Tools"
        )


        technology_columns = st.columns(
            len(project["technologies"])
        )


        for technology_index, technology in enumerate(
            project["technologies"]
        ):

            with technology_columns[
                technology_index
            ]:

                st.success(
                    technology
                )


        # --------------------------------------
        # PROJECT SEPARATOR
        # --------------------------------------

        if index < len(PROJECTS) - 1:

            st.divider()


    # ==========================================
    # PROJECT SUMMARY
    # ==========================================

    st.divider()

    st.header(
        "💡 My Project Focus"
    )


    col1, col2, col3 = st.columns(3)


    # --------------------------------------
    # CAD
    # --------------------------------------

    with col1:

        st.markdown(
            """
            ### 💻 CAD & Design

            Designing mechanical and agricultural
            machinery components using CATIA V5
            and 3DEXPERIENCE.
            """
        )


    # --------------------------------------
    # SIMULATION
    # --------------------------------------

    with col2:

        st.markdown(
            """
            ### 📊 Engineering Simulation

            Performing structural analysis and
            evaluating stress and deformation
            using ANSYS Workbench and FEA.
            """
        )


    # --------------------------------------
    # AGRICULTURAL TECHNOLOGY
    # --------------------------------------

    with col3:

        st.markdown(
            """
            ### 🌱 Smart Agriculture

            Exploring IoT, smart greenhouse
            automation, agricultural drones,
            and precision agriculture.
            """
        )


    # ==========================================
    # CAREER APPLICATION
    # ==========================================

    st.divider()

    st.header(
        "🎯 Application of My Skills"
    )

    st.write(
        "My projects have helped me develop practical knowledge "
        "in CAD modelling, mechanical component design, engineering "
        "simulation, agricultural machinery, automation, and "
        "emerging agricultural technologies. I am interested in "
        "applying these skills to real-world engineering and "
        "agricultural machinery development."
    )