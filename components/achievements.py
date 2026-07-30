import streamlit as st
from data import ACHIEVEMENTS, CERTIFICATIONS, MEMBERSHIPS, LEADERSHIP

def show():
    st.title("🏆 Achievements & activities")

st.write(
    "My achievements, leadership experience, professional memberships, "
    "certifications, and extracurricular activities."
)

st.divider()

st.header("🏆 Achievements")
cols = st.columns(2)

for i, achievement in enumerate(ACHIEVEMENTS):
    with cols[i % 2]:
        st.subheader(achievement["title"])
        st.write(achievement["description"])

st.divider()

st.header("📜 Certifications")
cert_cols = st.columns(2)

for i, cert in enumerate(CERTIFICATIONS):
    cert_cols[i % 2].success(f"✓ {cert}")

st.divider()

st.header("👨‍💼 Leadership experience")

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

st.header("🚀 Professional development")

st.write(
    "I continuously develop my technical and professional skills through internships, "
    "engineering projects, certifications, student activities, and leadership responsibilities."
)
