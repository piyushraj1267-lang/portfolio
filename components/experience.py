import streamlit as st
from data import EXPERIENCE


def show():
    st.title("💼 Experience")

    st.write(
        "My practical internship experience in agricultural engineering, "
        "farm machinery, tractor systems, testing, and soil and water conservation."
    )

    st.divider()

    for index, exp in enumerate(EXPERIENCE):
        st.header(f"Experience {index + 1}: {exp['job_title']}")
        st.write(f"**{exp['company']}**")
        st.write(f"📍 {exp['location']}")
        st.write(f"📅 {exp['duration']}")

        st.subheader("Key responsibilities")
        for item in exp["description"]:
            st.write(f"• {item}")

        st.divider()

    st.header("📌 Internship highlights")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
CFMTTI, Budni

• Tractor systems
• Tractor testing
• Farm machinery
• Preventive maintenance
• Performance evaluation
            """
        )

    with col2:
        st.success(
            """
ICAR-IISWC, Dehradun

• Soil conservation
• Water conservation
• Watershed management
• Irrigation practices
• Field surveys
            """
        )