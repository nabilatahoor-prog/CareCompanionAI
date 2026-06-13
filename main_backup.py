import streamlit as st
import pandas as pd

st.set_page_config(page_title="CareCompanionAI", page_icon="🏥", layout="wide")

# Custom CSS for beautiful look
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .css-1d391kg { background-color: #1a1a2e; }
    .stButton > button { background-color: #4CAF50; color: white; border-radius: 10px; }
    .stMetric { background-color: white; border-radius: 15px; padding: 15px; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# Sidebar Navigation
with st.sidebar:
    st.title("🏥 CareCompanionAI")
    st.divider()
    
    if st.button("📊 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"
    if st.button("💊 Medicines", use_container_width=True):
        st.session_state.page = "Medicines"
    if st.button("📅 Appointments", use_container_width=True):
        st.session_state.page = "Appointments"
    if st.button("📈 Health Timeline", use_container_width=True):
        st.session_state.page = "Health Timeline"
    if st.button("👤 Profile", use_container_width=True):
        st.session_state.page = "Profile"
    if st.button("🆘 SOS", use_container_width=True):
        st.session_state.page = "SOS"
    if st.button("👨‍👩‍👧 Caregiver", use_container_width=True):
        st.session_state.page = "Caregiver Dashboard"
    
    st.divider()
    st.caption("💡 Your Health Companion")

# DASHBOARD
if st.session_state.page == "Dashboard":
    st.title("📊 Dashboard")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("❤️ Heart Rate", "83 bpm", "Normal")
    c2.metric("🩸 Blood Pressure", "124/72", "Stable")
    c3.metric("👣 Today's Steps", "5,328", "Goal: 10,000")
    
    st.subheader("📋 Recent Activity")
    st.write("✅ Morning medications taken at 8:00 AM")
    st.write("💉 Blood sugar checked: 119 mg/dL")
    st.write("🏃 Walked 2,000 steps")
    
    st.subheader("📅 Today's Schedule")
    data = {'Time': ['8:00 AM', '1:00 PM', '6:00 PM'], 'Task': ['Take Aspirin', 'Lunch & Walk', 'Check BP'], 'Status': ['✅ Done', '⏰ Upcoming', '⏰ Upcoming']}
    st.dataframe(pd.DataFrame(data), use_container_width=True)

# MEDICINES
elif st.session_state.page == "Medicines":
    st.title("💊 Medicines")
    st.checkbox("Aspirin 81mg - Morning", value=True)
    st.checkbox("Vitamin D - Afternoon")
    st.checkbox("Blood Pressure - Evening")
    if st.button("✓ Mark All as Taken"):
        st.success("All medications taken!")

# APPOINTMENTS
elif st.session_state.page == "Appointments":
    st.title("📅 Appointments")
    st.info("**Dr. Smith** - Cardiology\n📅 June 15, 2026 at 10:00 AM")
    st.info("**Dr. Patel** - Blood Test\n📅 June 18, 2026 at 2:30 PM")
    with st.expander("➕ New Appointment"):
        st.text_input("Doctor")
        st.date_input("Date")
        st.time_input("Time")
        st.button("Schedule")

# HEALTH TIMELINE
elif st.session_state.page == "Health Timeline":
    st.title("📈 Health Timeline")
    bp = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'BP': [130, 128, 125, 122, 120]})
    st.line_chart(bp.set_index('Month'))

# PROFILE
elif st.session_state.page == "Profile":
    st.title("👤 Profile")
    st.write("**Name:** John Doe")
    st.write("**Age:** 65")
    st.write("**Blood Type:** A+")
    with st.form("edit"):
        name = st.text_input("Name", "John Doe")
        st.form_submit_button("Update")

# SOS
elif st.session_state.page == "SOS":
    st.title("🆘 SOS Emergency")
    st.error("⚠️ EMERGENCY ⚠️")
    if st.button("🚑 CALL 911", type="primary"):
        st.error("Calling emergency services...")

# CAREGIVER
elif st.session_state.page == "Caregiver Dashboard":
    st.title("👨‍👩‍👧 Caregiver Dashboard")
    c1, c2 = st.columns(2)
    c1.metric("Medication", "94%", "+2%")
    c2.metric("Check-in", "2 hours ago")
    st.checkbox("Review weekly report")
