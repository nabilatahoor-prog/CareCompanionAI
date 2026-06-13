import streamlit as st
import json
from pathlib import Path

class FirebaseConfig:
    def __init__(self):
        self.use_mock = True
        self.mock_data = {}
        self._check_firebase()
    
    def _check_firebase(self):
        key_path = Path(__file__).parent.parent.parent / 'firebase' / 'firebase-key.json'
        if key_path.exists():
            try:
                import firebase_admin
                from firebase_admin import credentials, firestore
                cred = credentials.Certificate(str(key_path))
                firebase_admin.initialize_app(cred)
                self.db = firestore.client()
                self.use_mock = False
                st.success("✅ Firebase connected!")
            except Exception as e:
                st.warning(f"Firebase not configured: {e}")
        else:
            st.info("📦 Using local storage (mock mode). Add firebase-key.json to enable cloud sync.")
    
    def get_db(self):
        return self.db if not self.use_mock else None
    
    def is_mock(self):
        return self.use_mock

firebase_config = FirebaseConfig()
