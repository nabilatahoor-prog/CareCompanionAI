from backend.emergency.sos_service import sos_service
from backend.emergency.emergency_contacts import emergency_contacts
import streamlit as st

def show():
    st.title("🆘 SOS Emergency")
    st.error("⚠️ ONLY USE IN REAL EMERGENCIES ⚠️")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚑 Call Ambulance (911)", type="primary", use_container_width=True):
            st.error("**CALLING 911...** Emergency services have been notified!")
            st.balloons()
    
    with col2:
        if st.button("📞 Call Caregiver", use_container_width=True):
            st.warning("Calling primary caregiver...")
    
    st.divider()
    st.subheader("📋 Emergency Contacts")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Primary Caregiver**")
        st.write("👤 Sarah (Daughter)")
        st.write("📞 (555) 234-5678")
    
    with col2:
        st.write("**Doctor**")
        st.write("👨‍⚕️ Dr. Smith")
        st.write("📞 (555) 123-4567")
    
    with st.expander("🏥 Medical Information for Responders"):
        st.write("**Blood Type:** A+")
        st.write("**Allergies:** Penicillin, Peanuts")
        st.write("**Conditions:** High Blood Pressure, Diabetes Type 2")
        st.write("**Medications:** Aspirin, Lisinopril, Metformin")
        st.write("**Primary Doctor:** Dr. Smith - (555) 123-4567")
