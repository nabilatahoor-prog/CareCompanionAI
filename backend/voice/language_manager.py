import streamlit as st

class LanguageManager:
    def __init__(self):
        self.supported_languages = {
            'en': 'English',
            'hi': 'हिन्दी (Hindi)',
            'es': 'Español (Spanish)',
            'ta': 'தமிழ் (Tamil)',
            'te': 'తెలుగు (Telugu)',
            'bn': 'বাংলা (Bengali)',
            'mr': 'मराठी (Marathi)',
            'gu': 'ગુજરાતી (Gujarati)',
            'kn': 'ಕನ್ನಡ (Kannada)',
            'ml': 'മലയാളം (Malayalam)'
        }
        
        # Set default language from session or English
        if 'language' not in st.session_state:
            st.session_state.language = 'en'
    
    def get_current_language(self):
        return st.session_state.get('language', 'en')
    
    def set_language(self, lang_code):
        if lang_code in self.supported_languages:
            st.session_state.language = lang_code
            return True
        return False
    
    def translate(self, key):
        """Get translation for a key in current language"""
        translations = self._get_translations()
        lang = self.get_current_language()
        
        if key in translations and lang in translations[key]:
            return translations[key][lang]
        elif key in translations and 'en' in translations[key]:
            return translations[key]['en']
        return key
    
    def _get_translations(self):
        """All translations for the app"""
        return {
            # Navigation
            'dashboard': {
                'en': 'Dashboard', 'hi': 'डैशबोर्ड', 'es': 'Panel', 'ta': 'டாஷ்போர்டு'
            },
            'medicines': {
                'en': 'Medicines', 'hi': 'दवाइयाँ', 'es': 'Medicinas', 'ta': 'மருந்துகள்'
            },
            'appointments': {
                'en': 'Appointments', 'hi': 'अपॉइंटमेंट', 'es': 'Citas', 'ta': 'சந்திப்புகள்'
            },
            'profile': {
                'en': 'Profile', 'hi': 'प्रोफाइल', 'es': 'Perfil', 'ta': 'சுயவிவரம்'
            },
            'sos': {
                'en': 'SOS', 'hi': 'एसओएस', 'es': 'SOS', 'ta': 'எஸ்ஓஎஸ்'
            },
            
            # Common UI
            'welcome': {
                'en': 'Welcome', 'hi': 'स्वागत है', 'es': 'Bienvenido', 'ta': 'வரவேற்கிறோம்'
            },
            'logout': {
                'en': 'Logout', 'hi': 'लॉगआउट', 'es': 'Cerrar sesión', 'ta': 'வெளியேறு'
            },
            'settings': {
                'en': 'Settings', 'hi': 'सेटिंग्स', 'es': 'Configuración', 'ta': 'அமைப்புகள்'
            },
            
            # Health metrics
            'heart_rate': {
                'en': 'Heart Rate', 'hi': 'हृदय गति', 'es': 'Frecuencia cardíaca', 'ta': 'இதய துடிப்பு'
            },
            'blood_pressure': {
                'en': 'Blood Pressure', 'hi': 'रक्तचाप', 'es': 'Presión arterial', 'ta': 'இரத்த அழுத்தம்'
            },
            'steps': {
                'en': 'Steps', 'hi': 'कदम', 'es': 'Pasos', 'ta': 'படிகள்'
            },
            
            # Emergency
            'emergency': {
                'en': 'Emergency', 'hi': 'आपातकाल', 'es': 'Emergencia', 'ta': 'அவசரநிலை'
            },
            'call_help': {
                'en': 'Call for Help', 'hi': 'मदद के लिए कॉल करें', 'es': 'Llamar para ayuda', 'ta': 'உதவிக்கு அழைக்கவும்'
            },
            
            # Voice assistant
            'voice_assistant': {
                'en': 'Voice Assistant', 'hi': 'वॉयस असिस्टेंट', 'es': 'Asistente de voz', 'ta': 'குரல் உதவியாளர்'
            },
            'click_to_speak': {
                'en': 'Click to Speak', 'hi': 'बोलने के लिए क्लिक करें', 'es': 'Haz clic para hablar', 'ta': 'பேச கிளிக் செய்யவும்'
            },
            
            # AI Assistant
            'ai_assistant': {
                'en': 'AI Assistant', 'hi': 'एआई असिस्टेंट', 'es': 'Asistente IA', 'ta': 'AI உதவியாளர்'
            },
            'ask_question': {
                'en': 'Ask me anything', 'hi': 'कुछ भी पूछें', 'es': 'Pregúntame cualquier cosa', 'ta': 'எதையும் கேளுங்கள்'
            }
        }
    
    def get_language_selector(self):
        """Display language selector in sidebar"""
        current_lang = self.get_current_language()
        lang_names = [f"{flag} {name}" for flag, name in [
            ('🇺🇸', 'English'), ('🇮🇳', 'हिन्दी'), ('🇪🇸', 'Español'),
            ('🇮🇳', 'தமிழ்'), ('🇮🇳', 'తెలుగు'), ('🇮🇳', 'বাংলা')
        ]]
        
        selected = st.selectbox(
            "🌐 Language / भाषा",
            lang_names,
            index=0
        )
        
        # Map selection to language code
        lang_map = {
            '🇺🇸 English': 'en', '🇮🇳 हिन्दी': 'hi', '🇪🇸 Español': 'es',
            '🇮🇳 தமிழ்': 'ta', '🇮🇳 తెలుగు': 'te', '🇮🇳 বাংলা': 'bn'
        }
        
        if selected in lang_map and lang_map[selected] != current_lang:
            self.set_language(lang_map[selected])
            st.rerun()

language_manager = LanguageManager()

# Helper function for easy translation
def _(key):
    """Shortcut for translation"""
    return language_manager.translate(key)
