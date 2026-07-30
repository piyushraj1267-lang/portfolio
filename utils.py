import streamlit as st


# ==========================================
# SECTION TITLE
# ==========================================

def section_title(title, subtitle=None):

    st.title(title)

    if subtitle:
        st.write(subtitle)


# ==========================================
# SKILL BADGE
# ==========================================

def skill_badge(skill):

    return f"""
    <span class="skill-badge">
        {skill}
    </span>
    """


# ==========================================
# DISPLAY SKILL BADGES
# ==========================================

def display_skill_badges(skills):

    badges = ""

    for skill in skills:

        badges += skill_badge(skill)

    st.markdown(
        f"""
        <div>
            {badges}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# DISPLAY BULLET LIST
# ==========================================

def display_bullet_list(items):

    for item in items:

        st.write(
            f"• {item}"
        )