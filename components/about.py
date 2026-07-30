import streamlit as st

from data import (
    PERSONAL_INFO,
    EDUCATION,
    LEADERSHIP,
    MEMBERSHIPS,
    LANGUAGES,
    AREAS_OF_INTEREST,
)


def show():
    st.title("👨‍🎓 About me")

    st.write(
        "Get to know more about my education, leadership experience, "
        "professional memberships, and career interests."
    )

    st.divider()

    st.header("About me")
    st.subheader(PERSONAL_INFO["name"])
    st.write(PERSONAL_INFO["summary"])

    st.write(
        f"I am currently pursuing **{EDUCATION['degree']}** at "
        f"**{EDUCATION['university']}**, Odisha."
    )

    st.divider()

    st.header("🎓 Education")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(EDUCATION["degree"])
        st.write(f"🏫 {EDUCATION['university']}")
        st.write(f"📍 {EDUCATION['location']}")

    with col2:
        st.metric("Status", EDUCATION["status"])
        st.write(f"Graduation: {EDUCATION['graduation']}")
        st.write(f"CGPA: {EDUCATION['cgpa']}")

    st.divider()

    st.header("👨‍💼 Leadership & positions of responsibility")

    for role in LEADERSHIP:
        st.subheader(role["title"])
        st.write(f"**{role['organization']}**")
        st.write(f"📅 {role['duration']}")
        st.write(role["description"])

        st.write("**Key responsibilities:**")
        for responsibility in role["responsibilities"]:
            st.write(f"• {responsibility}")

        st.divider()

    st.header("🤝 Professional memberships")

    for membership in MEMBERSHIPS:
        st.subheader(membership["organization"])
        st.write(f"**Role:** {membership['role']}")
        st.write(f"**Duration:** {membership['duration']}")
        st.write(membership["description"])

        st.divider()

    st.header("🎯 Areas of interest")

    cols = st.columns(3)
    for i, interest in enumerate(AREAS_OF_INTEREST):
        cols[i % 3].info(interest)

    st.divider()

    st.header("🌐 Languages")

    lang_cols = st.columns(len(LANGUAGES))
    for i, language in enumerate(LANGUAGES):
        lang_cols[i].success(language)