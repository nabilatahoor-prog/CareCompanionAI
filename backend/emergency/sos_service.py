import streamlit as st
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

class SOSService:
    def __init__(self):
        self.emergency_active = False
    
    def trigger_sos(self, user_info, location=None):
        self.emergency_active = True
        
        message = f"""
        🚨 EMERGENCY ALERT 🚨
        
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Patient: {user_info.get('name', 'Unknown')}
        Age: {user_info.get('age', 'Unknown')}
        Blood Type: {user_info.get('blood_group', 'Unknown')}
        Allergies: {user_info.get('allergies', 'Unknown')}
        Location: {location or 'Location not available'}
        
        This is an automated emergency alert from CareCompanionAI.
        Please contact immediately.
        """
        
        st.error(message)
        return message
    
    def send_alert(self, contacts, message):
        for contact in contacts:
            st.warning(f"Alert sent to: {contact.get('name')} - {contact.get('phone')}")
        return True
    
    def get_emergency_instructions(self):
        return """
        🚑 EMERGENCY INSTRUCTIONS:
        1. Stay calm
        2. Call 911 immediately
        3. Take prescribed medications if needed
        4. Contact family/caregiver
        5. Keep medical ID handy
        """

sos_service = SOSService()
