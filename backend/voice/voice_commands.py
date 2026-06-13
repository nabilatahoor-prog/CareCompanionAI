class VoiceCommands:
    def __init__(self):
        self.command_map = {
            'dashboard': ['dashboard', 'home', 'main', 'go to dashboard', 'show dashboard'],
            'medicines': ['medicines', 'medication', 'pills', 'drugs', 'show medicines'],
            'appointments': ['appointments', 'appointment', 'doctor', 'show appointments'],
            'health timeline': ['health timeline', 'timeline', 'health history'],
            'profile': ['profile', 'my profile', 'account'],
            'sos': ['sos', 'emergency', 'help', 'call for help', 'sos emergency'],
            'caregiver dashboard': ['caregiver', 'caregiver dashboard']
        }
    
    def parse_command(self, text):
        if not text:
            return None
        
        text = text.lower().strip()
        
        for page, triggers in self.command_map.items():
            for trigger in triggers:
                if trigger in text:
                    # Return formatted page name
                    if page == 'health timeline':
                        return 'Health Timeline'
                    elif page == 'caregiver dashboard':
                        return 'Caregiver Dashboard'
                    else:
                        return page.capitalize()
        return None

voice_commands = VoiceCommands()
