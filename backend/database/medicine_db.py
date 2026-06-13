import json
import uuid
from datetime import datetime
from pathlib import Path

class MedicineDB:
    def __init__(self):
        self.data_file = Path(__file__).parent.parent.parent / 'data' / 'medicines.json'
        self.data_file.parent.mkdir(exist_ok=True)
        self.medicines = {}
        self._load_data()
    
    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.medicines = json.load(f)
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.medicines, f, default=str)
    
    def add_medicine(self, user_id, name, dosage, time, frequency='daily'):
        med_id = str(uuid.uuid4())
        medicine = {
            'id': med_id,
            'name': name,
            'dosage': dosage,
            'time': time,
            'frequency': frequency,
            'created_at': datetime.now().isoformat(),
            'taken_history': []
        }
        
        if user_id not in self.medicines:
            self.medicines[user_id] = []
        
        self.medicines[user_id].append(medicine)
        self._save_data()
        return medicine
    
    def get_user_medicines(self, user_id):
        return self.medicines.get(user_id, [])
    
    def mark_taken(self, user_id, medicine_id):
        for med in self.medicines.get(user_id, []):
            if med['id'] == medicine_id:
                med['taken_history'].append({
                    'date': datetime.now().isoformat(),
                    'status': 'taken'
                })
                self._save_data()
                return True
        return False
    
    def delete_medicine(self, user_id, medicine_id):
        if user_id in self.medicines:
            self.medicines[user_id] = [m for m in self.medicines[user_id] if m['id'] != medicine_id]
            self._save_data()
            return True
        return False

medicine_db = MedicineDB()
