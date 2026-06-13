import json
import uuid
from datetime import datetime, timedelta
from pathlib import Path

class TimelineDB:
    def __init__(self):
        self.data_file = Path(__file__).parent.parent.parent / 'data' / 'timeline.json'
        self.data_file.parent.mkdir(exist_ok=True)
        self.entries = {}
        self._load_data()
    
    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.entries = json.load(f)
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.entries, f, default=str)
    
    def add_entry(self, user_id, metric_type, value, unit, notes=''):
        entry_id = str(uuid.uuid4())
        entry = {
            'id': entry_id,
            'type': metric_type,
            'value': value,
            'unit': unit,
            'notes': notes,
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().date().isoformat()
        }
        
        if user_id not in self.entries:
            self.entries[user_id] = []
        
        self.entries[user_id].append(entry)
        self._save_data()
        return entry
    
    def get_user_entries(self, user_id, days=30):
        entries = self.entries.get(user_id, [])
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        return [e for e in entries if e['timestamp'] >= cutoff]

timeline_db = TimelineDB()
