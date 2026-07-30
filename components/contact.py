import streamlit as st
from data import PERSONAL_INFO

def show():
    st.title("📩 Contact me")

st.write(
    "I am open to internship opportunities, entry-level roles, projects, and "
    "collaborations related to Agricultural Engineering, CAD/CAE, CATIA V5, "
    "Farm Machinery, and Agricultural Technology."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Contact information")
    st.write(f"📍 **Location:** {PERSONAL_INFO['location']}")
    st.write(f"📧 **Email:** {PERSONAL_INFO['email']}")
    st.write(f"📱 **Phone:** {PERSONAL_INFO['phone']}")

with col2:
    st.subheader("Professional links")
    st.link_button("🔗 LinkedIn", PERSONAL_INFO["linkedin"])
    st.link_button("💻 GitHub", PERSONAL_INFO["github"])
    st.link_button(
        "📧 Send Email",
        f"mailto:{PERSONAL_INFO['email']}"
    )

st.divider()

st.info(
    "Feel free to connect with me regarding internships, research, CAD design, "
    "agricultural machinery, farm mechanization, or engineering opportunities."
)
