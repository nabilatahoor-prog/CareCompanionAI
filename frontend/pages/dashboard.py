from backend.database.user_db import user_db
from backend.database.medicine_db import medicine_db
from backend.database.appointment_db import appointment_db
import streamlit as st
import pandas as pd

def show():
    st.title("📊 Dashboard")
    user_id = st.session_state.get("user_id")
    backend = st.session_state.get("backend", {})

    st.subheader("❤️ Health Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("❤️ Heart Rate", "83 bpm", "Normal")
    with col2:
        st.metric("🩸 Blood Pressure", "124/72", "Stable")
    with col3:
        st.metric("👟 Today Steps", "5,328", "Goal: 10,000")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("💨 O2 Level", "98%", "Normal")
    with col5:
        st.metric("🌡️ Temperature", "98.6°F", "Normal")
    with col6:
        st.metric("🩸 Blood Sugar", "119 mg/dL", "Normal")

    st.divider()
    st.subheader("📋 Recent Activity")

    if not user_id:
        st.write("✅ Morning medications taken at 8:00 AM")
        st.write("🩸 Blood sugar checked: 119 mg/dL")
        st.write("👟 Walked 2,000 steps")
        st.write("🔔 Evening medications reminder")
        st.subheader("📅 Today Schedule")
        sample = pd.DataFrame([
            {"Time": "8:00 AM", "Task": "Take Aspirin", "Status": "✅ Done"},
            {"Time": "1:00 PM", "Task": "Lunch & Walk", "Status": "🔔 Upcoming"},
            {"Time": "6:00 PM", "Task": "Check Blood Pressure", "Status": "🔔 Upcoming"},
        ])
        st.dataframe(sample, use_container_width=True)
        return

    user = user_db.get_user(user_id) or {}
    medicines = medicine_db.get_user_medicines(user_id)
    appointments = appointment_db.get_user_appointments(user_id)

    if medicines:
        for medicine in medicines[:5]:
            st.write(f"💊 {medicine.get('name','Medicine')} - {medicine.get('dosage','')} at {medicine.get('time','')}")
    else:
        st.info("No medicines added yet.")

    st.subheader("📅 Today Schedule")
    if appointments:
        st.dataframe(pd.DataFrame(appointments), use_container_width=True)
    else:
        st.info("No appointments scheduled yet.")

    st.divider()
    st.subheader("🤖 Ask CareCompanionAI")
    question = st.text_input("Ask a health question", placeholder="Example: What should I do before my appointment?")
    if st.button("Ask AI", type="primary"):
        if not question:
            st.error("Please enter a question.")
            return
        gemini_service = backend.get("gemini_service")
        run_async = backend.get("run_async")
        if not gemini_service or not run_async:
            st.error("Gemini service is not connected.")
            return
        context = {"user": user, "medicines": medicines, "appointments": appointments}
        with st.spinner("Thinking..."):
            response = run_async(gemini_service.health_chat(user_id=user_id, message=question, context=str(context)))
        st.success(response)
