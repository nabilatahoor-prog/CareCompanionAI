import streamlit as st

from frontend.components.navbar import show_navbar
from frontend.styles.theme import load_theme

from frontend.pages import dashboard
from frontend.pages import medicines
from frontend.pages import appointments
from frontend.pages import health_timeline
from frontend.pages import profile
from frontend.pages import sos
from frontend.pages import caregiver_dashboard
from backend.features.feature_bridge import render_prescription_scanner, render_voice_assistant, render_language_settings

st.set_page_config(
    page_title="CompanionCareAI",
    layout="wide"
)

load_theme()

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

elif page == "Prescription Scanner":
    render_prescription_scanner()

elif page == "Voice Assistant":
    render_voice_assistant()

elif page == "Language Settings":
    render_language_settings()
