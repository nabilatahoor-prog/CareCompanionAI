from backend.database.firebase_config import firebase_config
import json
import uuid
from datetime import datetime
from pathlib import Path


class MedicineDB:
    def __init__(self):
        self.db = firebase_config.get_db()
        self.data_file = (
            Path(__file__).parent.parent.parent
            / "data"
            / "medicines.json"
        )
        self.data_file.parent.mkdir(exist_ok=True)
        self.medicines = {}
        self._load_data()

    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, "r") as f:
                self.medicines = json.load(f)

    def _save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.medicines, f, default=str)

    def add_medicine(self, user_id, name, dosage, time, frequency="daily"):
        med_id = str(uuid.uuid4())
        medicine = {
            "id": med_id,
            "name": name,
            "dosage": dosage,
            "time": str(time),
            "frequency": frequency,
            "created_at": datetime.now().isoformat(),
            "taken_history": [],
        }

        if self.db:
            (
                self.db.collection("users")
                .document(user_id)
                .collection("medicines")
                .document(med_id)
                .set(medicine)
            )
            return medicine

        if user_id not in self.medicines:
            self.medicines[user_id] = []

        self.medicines[user_id].append(medicine)
        self._save_data()
        return medicine

    def get_user_medicines(self, user_id):
        if self.db:
            docs = (
                self.db.collection("users")
                .document(user_id)
                .collection("medicines")
                .stream()
            )
            return [doc.to_dict() for doc in docs]

        return self.medicines.get(user_id, [])

    def mark_taken(self, user_id, medicine_id):
        taken_entry = {
            "date": datetime.now().isoformat(),
            "status": "taken",
        }

        if self.db:
            ref = (
                self.db.collection("users")
                .document(user_id)
                .collection("medicines")
                .document(medicine_id)
            )

            doc = ref.get()
            if not doc.exists:
                return False

            data = doc.to_dict()
            history = data.get("taken_history", [])
            history.append(taken_entry)

            ref.update({"taken_history": history})
            return True

        for med in self.medicines.get(user_id, []):
            if med["id"] == medicine_id:
                med["taken_history"].append(taken_entry)
                self._save_data()
                return True

        return False

    def delete_medicine(self, user_id, medicine_id):
        if self.db:
            (
                self.db.collection("users")
                .document(user_id)
                .collection("medicines")
                .document(medicine_id)
                .delete()
            )
            return True

        if user_id in self.medicines:
            self.medicines[user_id] = [
                medicine
                for medicine in self.medicines[user_id]
                if medicine["id"] != medicine_id
            ]
            self._save_data()
            return True

        return False


medicine_db = MedicineDB()