import pyttsx3
import streamlit as st

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
    
    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            st.warning(f"TTS error: {e}")
    
    def get_voices(self):
        return self.engine.getProperty('voices')

text_to_speech = TextToSpeech()
