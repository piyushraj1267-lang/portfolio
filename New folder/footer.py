import streamlit as st
from data import PERSONAL_INFO

def render_footer():
    st.markdown("---")

    footer_html = f"""
    <div style="text-align:center; padding:20px;">
        <h2>Thank you for visiting my portfolio!</h2>

        <p>© 2026 {PERSONAL_INFO["name"]}. All Rights Reserved.</p>

        <p>
            <a href="{PERSONAL_INFO['linkedin']}" target="_blank">LinkedIn</a> |
            <a href="{PERSONAL_INFO['github']}" target="_blank">GitHub</a> |
            <a href="mailto:{PERSONAL_INFO['email']}">Email</a>
        </p>
    </div>
    """

    st.markdown(footer_html, unsafe_allow_html=True)