import re
from datetime import datetime

class Validators:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?1?\d{9,15}$'
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def validate_password(password):
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        return True, "Valid"
    
    @staticmethod
    def validate_blood_pressure(systolic, diastolic):
        if 90 <= systolic <= 200 and 60 <= diastolic <= 120:
            return True, "Normal range"
        return False, "Check with doctor"
    
    @staticmethod
    def validate_heart_rate(rate):
        if 40 <= rate <= 150:
            return True, "Normal"
        return False, "Abnormal range"

validators = Validators()
