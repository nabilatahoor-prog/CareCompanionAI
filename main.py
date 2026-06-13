import streamlit as st

st.set_page_config(
    page_title="CareCompanionAI",
    page_icon="🏥",
    layout="wide"
)

from frontend.components.navbar import show_navbar
from frontend.styles.theme import load_theme
from frontend.pages import dashboard, medicines, appointments, health_timeline, profile, sos, caregiver_dashboard

load_theme()

if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

page = show_navbar()

if page == "Dashboard":
    dashboard.show()
elif page == "Medicines":
    medicines.show()
elif page == "Appointments":
    appointments.show()
elif page == "Health Timeline":
    health_timeline.show()
elif page == "Profile":
    profile.show()
elif page == "SOS":
    sos.show()
elif page == "Caregiver Dashboard":
    caregiver_dashboard.show()
