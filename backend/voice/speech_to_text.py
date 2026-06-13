import streamlit as st
import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def listen(self, duration=5):
        with sr.Microphone() as source:
            st.info(f"🎤 Listening for {duration} seconds...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=duration)
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                return "Sorry, I couldn't understand that."
            except sr.RequestError:
                return "Speech service error."
    
    def get_voice_command(self):
        text = self.listen()
        if text:
            return text.lower()
        return None

speech_to_text = SpeechToText()
