import streamlit as st
from datetime import datetime

class CaregiverAlert:
    def __init__(self):
        self.alerts = []
    
    def send_alert(self, caregiver_info, alert_type, message):
        alert = {
            'timestamp': datetime.now().isoformat(),
            'type': alert_type,
            'caregiver': caregiver_info,
            'message': message,
            'status': 'sent'
        }
        self.alerts.append(alert)
        
        st.info(f"📱 Alert sent to caregiver {caregiver_info.get('name', 'Unknown')}")
        return alert
    
    def get_pending_alerts(self):
        return [a for a in self.alerts if a['status'] == 'sent']
    
    def acknowledge_alert(self, alert_id):
        for alert in self.alerts:
            if alert.get('id') == alert_id:
                alert['status'] = 'acknowledged'
                return True
        return False
    
    def schedule_check_in(self, user_id, interval_hours=24):
        st.success(f"✅ Check-in scheduled every {interval_hours} hours")

caregiver_alert = CaregiverAlert()
