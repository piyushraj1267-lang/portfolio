import streamlit as st
from data import PERSONAL_INFO

def show():
    st.divider()

st.markdown(
    f"""
```

### 🌾 {PERSONAL_INFO['name']}

**Final-Year B.Tech Agricultural Engineering Student**

CAD/CAE | CATIA V5 | 3DEXPERIENCE | ANSYS | Farm Machinery | Agricultural Technology

📍 {PERSONAL_INFO['location']}

© 2026 {PERSONAL_INFO['name']}. All rights reserved.
"""
)

st.caption("Built with Python and Streamlit")
