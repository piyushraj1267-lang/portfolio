import streamlit as st
from data import SKILLS


def show():
    st.title("🛠️ Technical skills")

    st.write(
        "My technical skills and knowledge across CAD design, engineering simulation, "
        "agricultural engineering, programming, and emerging agricultural technologies."
    )

    st.divider()

    for category, skills in SKILLS.items():
        st.header(category)

        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].success(skill)

    st.divider()

    st.header("🎯 Career interests")

    st.write(
        "I am interested in agricultural machinery, tractor design, CAD modelling, "
        "product design, engineering simulation, and precision agriculture."
    )