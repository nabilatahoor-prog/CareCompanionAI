from backend.database.firebase_config import firebase_config
from datetime import datetime

class SettingsDB:
    def __init__(self):
        self.db = firebase_config.get_db()
    
    def get_settings(self, user_id):
        if self.db is None:
            return {
                'language': 'en',
                'notifications': {
                    'medicine_reminders': True,
                    'appointment_reminders': True,
                    'sos_alerts': True
                },
                'voice_assistant': {
                    'enabled': True,
                    'speed': 'normal'
                }
            }
        try:
            doc = self.db.collection('users').document(user_id).collection('settings').document('user_settings').get()
            if doc.exists:
                return doc.to_dict()
            else:
                default = {
                    'language': 'en',
                    'notifications': {
                        'medicine_reminders': True,
                        'appointment_reminders': True,
                        'sos_alerts': True
                    },
                    'voice_assistant': {
                        'enabled': True,
                        'speed': 'normal'
                    }
                }
                self.db.collection('users').document(user_id).collection('settings').document('user_settings').set(default)
                return default
        except Exception as e:
            print(f"Error: {e}")
            return {}
    
    def update_settings(self, user_id, settings_data):
        if self.db is None:
            return True
        try:
            settings_data['updated_at'] = datetime.now()
            self.db.collection('users').document(user_id).collection('settings').document('user_settings').update(settings_data)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

settings_db = SettingsDB()