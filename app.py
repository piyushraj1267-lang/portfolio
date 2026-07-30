import streamlit as st

from components.hero import show as hero
from components.about import show as about
from components.skills import show as skills
from components.experience import show as experience
from components.projects import show as projects
from components.achievements import show as achievements
from components.contact import show as contact
from components.footer import show as footer

st.set_page_config(
page_title="Piyush Raj | Agricultural Engineering Portfolio",
page_icon="🌾",
layout="wide"
)

hero()
st.divider()

about()
st.divider()

skills()
st.divider()

experience()
st.divider()

projects()
st.divider()

achievements()
st.divider()

contact()
st.divider()

footer()
