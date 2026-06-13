import streamlit as st
from pathlib import Path


class FirebaseConfig:
    def __init__(self):
        self.use_mock = True
        self.db = None
        self._check_firebase()

    def _check_firebase(self):
        key_path = (
            Path(__file__).parent.parent.parent
            / "firebase"
            / "firebase-key.json"
        )

        if not key_path.exists():
            st.info(
                "Using local storage. Add firebase/firebase-key.json to enable Firebase."
            )
            return

        try:
            import firebase_admin
            from firebase_admin import credentials, firestore

            if not firebase_admin._apps:
                cred = credentials.Certificate(str(key_path))
                firebase_admin.initialize_app(cred)

            self.db = firestore.client()
            self.use_mock = False

        except Exception as e:
            st.warning(f"Firebase not configured: {e}")
            self.db = None
            self.use_mock = True

    def get_db(self):
        return self.db

    def is_mock(self):
        return self.use_mock


firebase_config = FirebaseConfig()