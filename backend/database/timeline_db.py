from backend.database.firebase_config import firebase_config
import json
import uuid
from datetime import datetime, timedelta
from pathlib import Path


class TimelineDB:
    def __init__(self):
        self.db = firebase_config.get_db()
        self.data_file = (
            Path(__file__).parent.parent.parent
            / "data"
            / "timeline.json"
        )
        self.data_file.parent.mkdir(exist_ok=True)
        self.entries = {}
        self._load_data()

    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, "r") as f:
                self.entries = json.load(f)

    def _save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.entries, f, default=str)

    def add_entry(self, user_id, metric_type, value, unit, notes=""):
        entry_id = str(uuid.uuid4())

        entry = {
            "id": entry_id,
            "type": metric_type,
            "value": value,
            "unit": unit,
            "notes": notes,
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().date().isoformat(),
        }

        if self.db:
            (
                self.db.collection("users")
                .document(user_id)
                .collection("timeline")
                .document(entry_id)
                .set(entry)
            )
            return entry

        if user_id not in self.entries:
            self.entries[user_id] = []

        self.entries[user_id].append(entry)
        self._save_data()
        return entry

    def get_user_entries(self, user_id, days=30):
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()

        if self.db:
            docs = (
                self.db.collection("users")
                .document(user_id)
                .collection("timeline")
                .where("timestamp", ">=", cutoff)
                .stream()
            )

            return [doc.to_dict() for doc in docs]

        entries = self.entries.get(user_id, [])
        return [
            entry
            for entry in entries
            if entry.get("timestamp", "") >= cutoff
        ]


timeline_db = TimelineDB()