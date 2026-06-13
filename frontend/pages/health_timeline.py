from backend.database.timeline_db import timeline_db
import streamlit as st
import pandas as pd

def show():
    st.title("📈 Health Timeline")
    
    st.subheader("🩸 Blood Pressure Trend")
    bp_data = pd.DataFrame({
        'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Systolic': [130, 128, 125, 122, 120, 118],
        'Diastolic': [85, 84, 82, 81, 80, 78]
    })
    st.line_chart(bp_data.set_index('Date'))
    
    st.subheader("⚖️ Weight Trend")
    weight_data = pd.DataFrame({
        'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Weight (lbs)': [165, 164, 163, 162, 161, 160]
    })
    st.line_chart(weight_data.set_index('Date'))
    
    st.subheader("📊 Health Summary")
    st.success("✅ Blood pressure is improving")
    st.success("✅ Weight is stable")
    st.info("📅 Next checkup: June 20, 2026")
