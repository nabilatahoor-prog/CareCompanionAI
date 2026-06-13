from backend.database.user_db import user_db
from backend.database.medicine_db import medicine_db
from backend.database.appointment_db import appointment_db
import streamlit as st
import pandas as pd

def show():
    st.title("📊 Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("❤️ Heart Rate", "83 bpm", "Normal")
    with col2:
        st.metric("🩸 Blood Pressure", "124/72", "Stable")
    with col3:
        st.metric("👣 Today's Steps", "5,328", "Goal: 10,000")
    
    st.subheader("📋 Recent Activity")
    st.write("✅ Morning medications taken at 8:00 AM")
    st.write("💉 Blood sugar checked: 119 mg/dL")
    st.write("🏃 Walked 2,000 steps")
    st.write("💊 Evening medications reminder")
    
    st.subheader("📅 Today's Schedule")
    schedule_data = pd.DataFrame({
        'Time': ['8:00 AM', '1:00 PM', '6:00 PM', '8:00 PM'],
        'Task': ['Take Aspirin', 'Lunch & Walk', 'Check Blood Pressure', 'Evening Medications'],
        'Status': ['✅ Done', '⏰ Upcoming', '⏰ Upcoming', '⏰ Upcoming']
    })
    st.dataframe(schedule_data, use_container_width=True)
