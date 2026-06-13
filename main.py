import asyncio
import streamlit as st

st.set_page_config(
    page_title="CareCompanionAI",
    page_icon="🏥",
    layout="wide"
)

# ==================== BACKEND CONNECTIONS ====================
from backend.database.user_db import user_db
from backend.database.medicine_db import medicine_db
from backend.database.appointment_db import appointment_db
from backend.database.timeline_db import timeline_db
from backend.database.settings_db import settings_db

from backend.services.gemini_service import gemini_service

from backend.voice.voice_commands import voice_commands
from backend.voice.browser_voice import browser_voice

from backend.scanner.prescription_ocr import prescription_ocr
from backend.scanner.medicine_extractor import medicine_extractor
from backend.scanner.prescription_parser import prescription_parser

from backend.emergency.sos_service import sos_service
from backend.emergency.emergency_contacts import emergency_contacts


# ==================== SESSION STATE ====================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "user_data" not in st.session_state:
    st.session_state.user_data = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# ==================== HELPERS ====================
def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return loop.run_until_complete(coro)


# ==================== BACKEND REGISTRY ====================
st.session_state.backend = {
    "user_db": user_db,
    "medicine_db": medicine_db,
    "appointment_db": appointment_db,
    "timeline_db": timeline_db,
    "settings_db": settings_db,
    "gemini_service": gemini_service,
    "voice_commands": voice_commands,
    "browser_voice": browser_voice,
    "prescription_ocr": prescription_ocr,
    "medicine_extractor": medicine_extractor,
    "prescription_parser": prescription_parser,
    "sos_service": sos_service,
    "emergency_contacts": emergency_contacts,
    "auth_service": user_db,
    "run_async": run_async,
    "user_id": st.session_state.user_id,
    "authenticated": st.session_state.authenticated,
}


# ==================== FRONTEND IMPORTS ====================
from frontend.components.navbar import show_navbar
from frontend.styles.theme import load_theme
from frontend.pages import (
    dashboard,
    medicines,
    appointments,
    health_timeline,
    profile,
    sos,
    caregiver_dashboard,
)

load_theme()


# ==================== AUTHENTICATION ====================
if not st.session_state.authenticated:
    st.title("CareCompanionAI")

    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

    with login_tab:
        st.subheader("Login")

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login", type="primary"):
            user = user_db.verify_user(email, password)

            if user:
                st.session_state.authenticated = True
                st.session_state.user_id = user["user_id"]
                st.session_state.user_data = user
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid email or password")

    with signup_tab:
        st.subheader("Create Account")

        name = st.text_input("Full Name", key="signup_name")
        age = st.number_input("Age", min_value=18, max_value=120, value=65)
        blood_group = st.selectbox(
            "Blood Group",
            ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        )
        allergies = st.text_area("Allergies", key="signup_allergies")
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )

        if st.button("Create Account", type="primary"):
            if not name or not signup_email or not signup_password:
                st.error("Please fill all required fields")
            else:
                user = user_db.create_user(
                    signup_email,
                    signup_password,
                    name,
                    age,
                    blood_group,
                    allergies
                )

                if user:
                    st.session_state.authenticated = True
                    st.session_state.user_id = user["user_id"]
                    st.session_state.user_data = user
                    st.success("Account created successfully!")
                    st.rerun()
                else:
                    st.error("User already exists")

    st.stop()


# ==================== NAVIGATION ====================
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