import streamlit as st

def show():
    st.title("🚀 Projects")

st.write(
    "A collection of my major academic and technical projects in agricultural engineering, "
    "CAD design, farm machinery, and smart agriculture."
)

st.divider()

# Project 1
st.header("1. Smart greenhouse automation system")
st.write("**Category:** Smart Agriculture & IoT")

st.write(
    "Developed a smart greenhouse automation system using Arduino and sensors to monitor "
    "and control environmental conditions such as irrigation and greenhouse climate."
)

st.subheader("Key features")
c1, c2, c3 = st.columns(3)
c1.info("Arduino")
c2.info("Sensors")
c3.info("Automation")
c1.info("Irrigation control")
c2.info("Environmental monitoring")
c3.info("Smart agriculture")

st.subheader("Technologies used")
t1, t2, t3, t4 = st.columns(4)
t1.success("Arduino")
t2.success("IoT")
t3.success("Sensors")
t4.success("Automation")

st.divider()

# Project 2
st.header("2. Automatic lawn mower")
st.write("**Category:** Agricultural Machinery")

st.write(
    "Designed and developed an automatic lawn mower prototype with a motor-driven cutting mechanism, "
    "battery system, and mechanical frame for efficient grass cutting operations."
)

st.subheader("Key features")
c1, c2, c3 = st.columns(3)
c1.info("Battery system")
c2.info("Electric motor")
c3.info("Cutting mechanism")
c1.info("Mechanical frame")
c2.info("Automatic operation")
c3.info("Farm machinery design")

st.subheader("Technologies used")
t1, t2, t3 = st.columns(3)
t1.success("Mechanical design")
t2.success("Electric drive")
t3.success("Farm machinery")

st.divider()

# Project 3
st.header("3. Tractor component design and assembly using CATIA V5")
st.write("**Category:** CAD & Product Design")

st.write(
    "Designed multiple tractor components using CATIA V5 and created assembly models of tractor parts. "
    "This project focused on 3D modelling, part design, and assembly design of agricultural machinery components."
)

st.subheader("Components designed")
c1, c2, c3 = st.columns(3)
c1.info("Wheel hub")
c2.info("Left lift arm")
c3.info("Gearbox cover")
c1.info("Clutch housing")
c2.info("Steering components")
c3.info("Tractor assembly")

st.subheader("Technologies used")
t1, t2, t3, t4 = st.columns(4)
t1.success("CATIA V5")
t2.success("Part design")
t3.success("Assembly design")
t4.success("3D modelling")

st.divider()

st.header("🎯 Project outcome")

st.write(
    "These projects strengthened my practical skills in CAD modelling, tractor component design, "
    "mechanical assembly, farm machinery development, automation, and smart agricultural systems. "
    "They also improved my understanding of product design and agricultural engineering applications."
)
