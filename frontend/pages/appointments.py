import streamlit as st
from datetime import datetime

def show():
    st.title("📅 Appointments")
    
    st.subheader("🏥 Upcoming Appointments")
    
    # Appointment 1
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown("""
            <div style='background: white; border-radius: 15px; padding: 20px; margin: 10px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
                <h3 style='color: #2c3e50; margin: 0;'>👨‍⚕️ Dr. Sarah Smith</h3>
                <p style='color: #666;'><strong>🏥 Cardiology</strong></p>
                <p>📅 <strong>Date:</strong> Tuesday, June 15, 2026</p>
                <p>⏰ <strong>Time:</strong> 10:00 AM</p>
                <p>📍 <strong>Location:</strong> City Hospital, Room 304</p>
                <p>📞 <strong>Phone:</strong> (555) 123-4567</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='background: #4CAF50; border-radius: 15px; padding: 20px; text-align: center;'>
                <h2 style='color: white; margin: 0;'>15</h2>
                <p style='color: white; margin: 0;'>JUN</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🔔 Remind", key="remind1", use_container_width=True):
                st.success("Reminder set for June 15!")
    
    # Appointment 2
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown("""
            <div style='background: white; border-radius: 15px; padding: 20px; margin: 10px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
                <h3 style='color: #2c3e50; margin: 0;'>👩‍⚕️ Dr. Priya Patel</h3>
                <p style='color: #666;'><strong>🧪 Blood Test</strong></p>
                <p>📅 <strong>Date:</strong> Thursday, June 18, 2026</p>
                <p>⏰ <strong>Time:</strong> 2:30 PM</p>
                <p>📍 <strong>Location:</strong> Wellness Center, Lab 2B</p>
                <p>⚠️ <strong>Instructions:</strong> Fast for 8 hours before test</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='background: #2196F3; border-radius: 15px; padding: 20px; text-align: center;'>
                <h2 style='color: white; margin: 0;'>18</h2>
                <p style='color: white; margin: 0;'>JUN</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🔔 Remind", key="remind2", use_container_width=True):
                st.success("Reminder set for June 18!")
    
    st.divider()
    
    # Schedule New Appointment
    st.subheader("➕ Schedule New Appointment")
    
    with st.expander("📝 Book an Appointment", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            doctor = st.text_input("Doctor Name")
            specialty = st.selectbox("Specialty", ["Cardiology", "General Medicine", "Blood Test", "Eye Checkup", "Dental"])
            date = st.date_input("Date")
        with col2:
            time = st.time_input("Time")
            location = st.text_input("Location")
            notes = st.text_area("Notes")
        
        if st.button("✅ Book Appointment", type="primary"):
            if doctor:
                st.success(f"Appointment booked with {doctor} on {date} at {time}!")
                st.balloons()
            else:
                st.error("Please enter doctor name")
    
    with st.expander("💡 Appointment Tips"):
        st.info("""
        ✅ Arrive 15 minutes early
        ✅ Bring your insurance card
        ✅ Make a list of questions
        ✅ Bring current medications list
        """)
