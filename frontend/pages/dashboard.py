from backend.database.user_db import user_db
from backend.database.medicine_db import medicine_db
from backend.database.appointment_db import appointment_db
import streamlit as st
import pandas as pd


def show():
    st.title("📊 Dashboard")

    user_id = st.session_state.get("user_id")
    backend = st.session_state.get("backend", {})

    if not user_id:
        st.warning("Please log in to view your dashboard.")
        return

    user = user_db.get_user(user_id) or {}
    medicines = medicine_db.get_user_medicines(user_id)
    appointments = appointment_db.get_user_appointments(user_id)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💊 Medicines", len(medicines))
    with col2:
        st.metric("📅 Appointments", len(appointments))
    with col3:
        st.metric("👤 User", user.get("name", "User"))

    st.subheader("📋 Recent Activity")
    if medicines:
        for medicine in medicines[:5]:
            st.write(
                f"💊 {medicine.get('name', 'Medicine')} - "
                f"{medicine.get('dosage', '')} at {medicine.get('time', '')}"
            )
    else:
        st.info("No medicines added yet.")

    st.subheader("📅 Today's Schedule")
    if appointments:
        schedule_data = pd.DataFrame(appointments)
        st.dataframe(schedule_data, use_container_width=True)
    else:
        st.info("No appointments scheduled yet.")

    st.divider()

    st.subheader("🤖 Ask CareCompanionAI")

    question = st.text_input(
        "Ask a health-related question",
        placeholder="Example: What should I remember before my next appointment?",
    )

    if st.button("Ask AI", type="primary"):
        if not question:
            st.error("Please enter a question.")
            return

        gemini_service = backend.get("gemini_service")
        run_async = backend.get("run_async")

        if not gemini_service or not run_async:
            st.error("Gemini service is not connected.")
            return

        context = {
            "user": user,
            "medicines": medicines,
            "appointments": appointments,
        }

        with st.spinner("Thinking..."):
            response = run_async(
                gemini_service.health_chat(
                    user_id=user_id,
                    message=question,
                    context=str(context),
                )
            )

        st.success(response)