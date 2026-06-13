import streamlit as st

class VoiceAssistant:
    def __init__(self):
        self.commands = {
            'dashboard': ['dashboard', 'home', 'main', 'go to dashboard'],
            'medicines': ['medicines', 'medication', 'pills', 'show medicines'],
            'appointments': ['appointments', 'appointment', 'doctor visit'],
            'health_timeline': ['health timeline', 'timeline', 'health history'],
            'profile': ['profile', 'my profile', 'account'],
            'sos': ['sos', 'emergency', 'help', 'call for help'],
            'caregiver_dashboard': ['caregiver', 'caregiver dashboard']
        }
    
    def parse_command(self, text):
        if not text:
            return None
        text = text.lower().strip()
        for page, triggers in self.commands.items():
            for trigger in triggers:
                if trigger in text:
                    return page
        return None
    
    def show_ui(self):
        st.write("### 🎤 Voice Command Center")
        st.write("Type your command below:")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            command = st.text_input("Command:", key="voice_cmd", placeholder="e.g., Go to dashboard")
        with col2:
            submit = st.button("Execute", use_container_width=True)
        
        if submit and command:
            return command
        return None

voice_assistant = VoiceAssistant()
