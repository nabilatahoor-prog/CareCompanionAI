import streamlit as st
import hashlib
import json
from datetime import datetime
from pathlib import Path

class UserDB:
    def __init__(self):
        self.users = {}
        self.data_file = Path(__file__).parent.parent.parent / 'data' / 'users.json'
        self.data_file.parent.mkdir(exist_ok=True)
        self._load_data()
    
    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.users = json.load(f)
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.users, f, default=str)
    
    def create_user(self, email, password, name, age, blood_group, allergies):
        user_id = email.replace('.', '_').replace('@', '_')
        if user_id in self.users:
            return None
        
        hashed = hashlib.sha256(password.encode()).hexdigest()
        user_data = {
            'user_id': user_id,
            'email': email,
            'name': name,
            'age': age,
            'blood_group': blood_group,
            'allergies': allergies,
            'created_at': datetime.now().isoformat(),
            'password_hash': hashed
        }
        self.users[user_id] = user_data
        self._save_data()
        return user_data
    
    def verify_user(self, email, password):
        user_id = email.replace('.', '_').replace('@', '_')
        hashed = hashlib.sha256(password.encode()).hexdigest()
        
        if user_id in self.users and self.users[user_id]['password_hash'] == hashed:
            return self.users[user_id]
        return None
    
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def update_user(self, user_id, updates):
        if user_id in self.users:
            self.users[user_id].update(updates)
            self._save_data()
            return self.users[user_id]
        return None

user_db = UserDB()

# Session helpers
def get_current_user():
    return st.session_state.get('user')

def set_current_user(user):
    st.session_state.user = user

def logout():
    if 'user' in st.session_state:
        del st.session_state.user
