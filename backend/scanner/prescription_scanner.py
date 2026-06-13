import cv2
import numpy as np
import pytesseract
import base64
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class PrescriptionScanner:
    def preprocess_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray, h=10)
        _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh

    def extract_text(self, image_data):
        try:
            if isinstance(image_data, str):
                if "," in image_data:
                    image_data = image_data.split(",")[1]
                img_bytes = base64.b64decode(image_data)
                img_array = np.frombuffer(img_bytes, dtype=np.uint8)
                image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            else:
                image = image_data
            processed = self.preprocess_image(image)
            return pytesseract.image_to_string(processed, config="--oem 3 --psm 6")
        except Exception as e:
            return f"Error: {str(e)}"

    def parse_prescription(self, text):
        medicines = []
        pattern = re.compile(
            r"([A-Za-z][A-Za-z\s\-]+(?:mg|mcg|ml|g)?)\s*"
            r"(\d+(?:\.\d+)?(?:mg|mcg|ml|g)?)\s*"
            r"(once|twice|thrice|\d+\s*times?)?\s*"
            r"(daily|morning|evening|night|after\s*food|before\s*food)?",
            re.IGNORECASE
        )
        for line in text.strip().split("\n"):
            line = line.strip()
            if len(line) < 3:
                continue
            match = pattern.search(line)
            if match:
                medicines.append({
                    "name": (match.group(1) or line).strip(),
                    "dosage": match.group(2) or "As prescribed",
                    "frequency": match.group(3) or "Once daily",
                    "timing": match.group(4) or "After food",
                    "raw_line": line
                })
            elif any(c.isalpha() for c in line):
                medicines.append({
                    "name": line, "dosage": "See prescription",
                    "frequency": "As directed", "timing": "As directed",
                    "raw_line": line
                })
        return {"medicines": medicines, "raw_text": text, "total_medicines": len(medicines)}

    def scan_prescription(self, image_data):
        raw_text = self.extract_text(image_data)
        return self.parse_prescription(raw_text)

scanner = PrescriptionScanner()
