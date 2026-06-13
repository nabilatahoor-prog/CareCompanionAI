import streamlit as st

def show_navbar():
    st.sidebar.title("🏥 CareCompanionAI")
    st.sidebar.divider()
    
    if st.sidebar.button("📊 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"
        st.rerun()
    if st.sidebar.button("💊 Medicines", use_container_width=True):
        st.session_state.page = "Medicines"
        st.rerun()
    if st.sidebar.button("📅 Appointments", use_container_width=True):
        st.session_state.page = "Appointments"
        st.rerun()
    if st.sidebar.button("📈 Health Timeline", use_container_width=True):
        st.session_state.page = "Health Timeline"
        st.rerun()
    if st.sidebar.button("👤 Profile", use_container_width=True):
        st.session_state.page = "Profile"
        st.rerun()
    if st.sidebar.button("🆘 SOS", use_container_width=True):
        st.session_state.page = "SOS"
        st.rerun()
    if st.sidebar.button("👨‍👩‍👧 Caregiver Dashboard", use_container_width=True):
        st.session_state.page = "Caregiver Dashboard"
        st.rerun()
    
    st.sidebar.divider()
    st.sidebar.caption("💡 Your Health Companion")
    
    return st.session_state.get("page", "Dashboard")
