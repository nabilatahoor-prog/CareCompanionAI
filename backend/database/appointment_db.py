from backend.database.firebase_config import firebase_config
import json
import uuid
from datetime import datetime
from pathlib import Path


class AppointmentDB:
    def __init__(self):
        self.db = firebase_config.get_db()
        self.data_file = (
            Path(__file__).parent.parent.parent
            / "data"
            / "appointments.json"
        )
        self.data_file.parent.mkdir(exist_ok=True)
        self.appointments = {}
        self._load_data()

    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, "r") as f:
                self.appointments = json.load(f)

    def _save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.appointments, f, default=str)

    def add_appointment(
        self,
        user_id,
        doctor_name,
        specialty,
        date,
        time,
        location,
        notes="",
    ):
        appointment_id = str(uuid.uuid4())

        appointment = {
            "id": appointment_id,
            "doctor_name": doctor_name,
            "specialty": specialty,
            "date": str(date),
            "time": str(time),
            "location": location,
            "notes": notes,
            "created_at": datetime.now().isoformat(),
            "reminder_set": False,
        }

        if self.db:
            (
                self.db.collection("users")
                .document(user_id)
                .collection("appointments")
                .document(appointment_id)
                .set(appointment)
            )
            return appointment

        if user_id not in self.appointments:
            self.appointments[user_id] = []

        self.appointments[user_id].append(appointment)
        self._save_data()
        return appointment

    def get_user_appointments(self, user_id):
        if self.db:
            docs = (
                self.db.collection("users")
                .document(user_id)
                .collection("appointments")
                .stream()
            )
            return [doc.to_dict() for doc in docs]

        return self.appointments.get(user_id, [])

    def set_reminder(self, user_id, appointment_id):
        if self.db:
            ref = (
                self.db.collection("users")
                .document(user_id)
                .collection("appointments")
                .document(appointment_id)
            )

            doc = ref.get()
            if not doc.exists:
                return False

            ref.update({"reminder_set": True})
            return True

        for appointment in self.appointments.get(user_id, []):
            if appointment["id"] == appointment_id:
                appointment["reminder_set"] = True
                self._save_data()
                return True

        return False

    def delete_appointment(self, user_id, appointment_id):
        if self.db:
            (
                self.db.collection("users")
                .document(user_id)
                .collection("appointments")
                .document(appointment_id)
                .delete()
            )
            return True

        if user_id in self.appointments:
            self.appointments[user_id] = [
                appointment
                for appointment in self.appointments[user_id]
                if appointment["id"] != appointment_id
            ]
            self._save_data()
            return True

        return False


appointment_db = AppointmentDB()