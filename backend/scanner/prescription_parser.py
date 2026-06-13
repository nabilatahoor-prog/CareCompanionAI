import json
from datetime import datetime

class PrescriptionParser:
    def parse(self, text):
        result = {
            'doctor': None,
            'patient': None,
            'date': None,
            'medicines': [],
            'instructions': []
        }
        
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            
            if 'Dr.' in line or 'Doctor' in line:
                result['doctor'] = line
            
            if 'Patient' in line or 'Name:' in line:
                result['patient'] = line
            
            if 'Date:' in line:
                result['date'] = line
            
            if any(keyword in line.lower() for keyword in ['mg', 'tablet', 'capsule', 'ml']):
                result['medicines'].append(line)
            
            if any(keyword in line.lower() for keyword in ['take', 'with food', 'empty stomach', 'daily']):
                result['instructions'].append(line)
        
        return result
    
    def to_json(self, parsed_data):
        return json.dumps(parsed_data, indent=2)

prescription_parser = PrescriptionParser()
