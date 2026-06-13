import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.current_language = "en"
        self.language_map = {
            "english": "en", "hindi": "hi", "telugu": "te",
            "tamil": "ta", "kannada": "kn", "marathi": "mr",
            "bengali": "bn", "gujarati": "gu"
        }
        self.sr_language_map = {
            "en": "en-IN", "hi": "hi-IN", "te": "te-IN",
            "ta": "ta-IN", "kn": "kn-IN", "mr": "mr-IN",
            "bn": "bn-IN", "gu": "gu-IN"
        }

    def set_language(self, lang_name):
        lang = lang_name.lower()
        if lang in self.language_map:
            self.current_language = self.language_map[lang]
        elif lang in self.language_map.values():
            self.current_language = lang
        return self.current_language

    def speak(self, text, lang=None):
        target_lang = lang or self.current_language
        try:
            if target_lang != "en":
                translated = GoogleTranslator(source="en", target=target_lang).translate(text)
                self.engine.say(translated)
            else:
                self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"TTS error: {e}")
            self.engine.say(text)
            self.engine.runAndWait()

    def listen(self):
        sr_lang = self.sr_language_map.get(self.current_language, "en-IN")
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
                text = self.recognizer.recognize_google(audio, language=sr_lang)
                if self.current_language != "en":
                    english_text = GoogleTranslator(source=self.current_language, target="en").translate(text)
                    return {"original": text, "english": english_text, "lang": self.current_language}
                return {"original": text, "english": text, "lang": "en"}
        except sr.WaitTimeoutError:
            return {"error": "No speech detected. Please try again."}
        except sr.UnknownValueError:
            return {"error": "Could not understand. Please speak clearly."}
        except Exception as e:
            return {"error": str(e)}

    def translate_response(self, text, target_lang=None):
        lang = target_lang or self.current_language
        if lang == "en":
            return text
        try:
            return GoogleTranslator(source="en", target=lang).translate(text)
        except:
            return text

voice_assistant = VoiceAssistant()
