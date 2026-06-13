import streamlit as st

def show():
    st.title("👨‍👩‍👧 Caregiver Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💊 Medication Adherence", "94%", "+2%")
    with col2:
        st.metric("⏰ Last Check-in", "2 hours ago")
    with col3:
        st.metric("📅 Upcoming Appointments", "2")
    with col4:
        st.metric("❤️ Health Score", "85/100", "+5")
    
    st.subheader("🔔 Recent Alerts")
    st.warning("⚠️ Blood pressure slightly elevated (128/85) - June 12, 2026")
    st.success("✅ Morning medications taken - June 12, 2026")
    st.info("📅 Follow-up appointment scheduled - June 15, 2026")
    
    st.subheader("✅ Care Tasks")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Review weekly health report")
        st.checkbox("Schedule follow-up with Dr. Smith")
        st.checkbox("Order medication refill")
    with col2:
        st.checkbox("Check blood pressure daily")
        st.checkbox("Monitor blood sugar levels")
        st.checkbox("Prepare weekly medication box")
    
    if st.button("📊 Generate Weekly Report", type="primary"):
        st.success("Weekly report generated and sent to caregiver's email!")
        st.balloons()
