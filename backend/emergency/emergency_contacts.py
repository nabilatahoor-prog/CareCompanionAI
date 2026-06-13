import json
from pathlib import Path

class EmergencyContacts:
    def __init__(self):
        self.data_file = Path(__file__).parent.parent.parent / 'data' / 'emergency_contacts.json'
        self.data_file.parent.mkdir(exist_ok=True)
        self.contacts = {}
        self._load_data()
    
    def _load_data(self):
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.contacts = json.load(f)
    
    def _save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def add_contact(self, user_id, name, relationship, phone, email=''):
        if user_id not in self.contacts:
            self.contacts[user_id] = []
        
        contact = {
            'name': name,
            'relationship': relationship,
            'phone': phone,
            'email': email,
            'is_primary': len(self.contacts[user_id]) == 0
        }
        self.contacts[user_id].append(contact)
        self._save_data()
        return contact
    
    def get_contacts(self, user_id):
        return self.contacts.get(user_id, [])
    
    def get_primary_contact(self, user_id):
        contacts = self.get_contacts(user_id)
        for contact in contacts:
            if contact.get('is_primary'):
                return contact
        return contacts[0] if contacts else None
    
    def delete_contact(self, user_id, contact_name):
        if user_id in self.contacts:
            self.contacts[user_id] = [c for c in self.contacts[user_id] if c['name'] != contact_name]
            self._save_data()
            return True
        return False

emergency_contacts = EmergencyContacts()
