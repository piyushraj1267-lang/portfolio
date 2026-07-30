import streamlit as st
from pathlib import Path
from data import PERSONAL_INFO

def show():
    st.title(PERSONAL_INFO["name"])
st.subheader(PERSONAL_INFO["title"])
st.write(PERSONAL_INFO["headline"])

col1, col2 = st.columns([1, 2])

with col1:
    image_path = Path(PERSONAL_INFO["profile_image"])
    if image_path.exists():
        st.image(str(image_path), width=250)
    else:
        st.warning("Profile image not found")

with col2:
    st.write(PERSONAL_INFO["summary"])
    st.write(f"📍 {PERSONAL_INFO['location']}")
    st.write(f"🎓 {PERSONAL_INFO['university']}")

    # Social links
    c1, c2, c3 = st.columns(3)

    with c1:
        st.link_button("LinkedIn", PERSONAL_INFO["linkedin"])

    with c2:
        st.link_button("GitHub", PERSONAL_INFO["github"])

    with c3:
        st.link_button(
            "Email",
            f"mailto:{PERSONAL_INFO['email']}"
        )

resume_path = Path(PERSONAL_INFO["resume"])
if resume_path.exists():
    with open(resume_path, "rb") as file:
        st.download_button(
            "📄 Download Resume",
            file,
            file_name="Piyush_Raj_Resume.pdf",
            mime="application/pdf"
        )

st.divider()

st.header("Core interests")

c1, c2, c3, c4 = st.columns(4)
c1.info("🚜 Farm machinery")
c2.info("💻 CAD / CAE")
c3.info("🚁 Agricultural drones")
c4.info("🌱 Smart agriculture")
