import streamlit as st
from PIL import Image
import pytesseract
import re

class PrescriptionOCR:
    def __init__(self):
        self.setup_tesseract()
    
    def setup_tesseract(self):
        try:
            pytesseract.get_tesseract_version()
            self.available = True
        except:
            self.available = False
            st.warning("Tesseract not installed. Install from: https://github.com/UB-Mannheim/tesseract/wiki")
    
    def extract_text(self, image):
        if not self.available:
            return "OCR not available. Please install Tesseract."
        
        try:
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            return f"OCR error: {e}"
    
    def extract_medicines(self, image):
        text = self.extract_text(image)
        medicines = []
        
        patterns = [
            r'([A-Z][a-z]+)\s+(\d+\s*(mg|mcg|ml))',
            r'(Aspirin|Paracetamol|Ibuprofen|Metformin|Lisinopril)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    medicines.append(match[0])
                else:
                    medicines.append(match)
        
        return list(set(medicines))

prescription_ocr = PrescriptionOCR()
