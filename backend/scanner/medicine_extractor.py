import re

class MedicineExtractor:
    def __init__(self):
        self.medicine_keywords = [
            'aspirin', 'paracetamol', 'ibuprofen', 'metformin',
            'lisinopril', 'atorvastatin', 'amoxicillin', 'azithromycin'
        ]
    
    def extract_from_text(self, text):
        medicines = []
        text_lower = text.lower()
        
        for medicine in self.medicine_keywords:
            if medicine in text_lower:
                medicines.append(medicine.title())
        
        dosage_pattern = r'(\d+(?:\.\d+)?)\s*(mg|mcg|ml|g)'
        dosages = re.findall(dosage_pattern, text_lower)
        
        return {
            'medicines': medicines,
            'dosages': [f"{d[0]} {d[1]}" for d in dosages],
            'raw_text': text
        }
    
    def suggest_schedule(self, medicines):
        schedule = {}
        default_times = ['08:00', '13:00', '20:00']
        
        for i, med in enumerate(medicines):
            schedule[med] = default_times[i % len(default_times)]
        
        return schedule

medicine_extractor = MedicineExtractor()
