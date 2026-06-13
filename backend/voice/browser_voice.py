import streamlit as st
import streamlit.components.v1 as components

class BrowserVoiceAssistant:
    def __init__(self):
        self.recognized_text = None
    
    def show_microphone(self):
        # HTML/JavaScript for browser-based voice recording
        microphone_html = '''
        <div id="voice-container">
            <button id="record-btn" style="
                background-color: #4CAF50;
                color: white;
                padding: 15px 30px;
                font-size: 18px;
                border: none;
                border-radius: 50px;
                cursor: pointer;
                margin: 10px;
                width: 100%;
            ">
                🎤 Click to Speak
            </button>
            <div id="result" style="
                margin-top: 20px;
                padding: 10px;
                background-color: #f0f2f6;
                border-radius: 10px;
                min-height: 60px;
            "></div>
        </div>
        
        <script>
        const recordBtn = document.getElementById('record-btn');
        const resultDiv = document.getElementById('result');
        let recognition = null;
        
        // Check if browser supports SpeechRecognition
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';
            
            recognition.onstart = function() {
                recordBtn.style.backgroundColor = '#ff4444';
                recordBtn.innerHTML = '🔴 Listening... Speak now';
                resultDiv.innerHTML = '🎤 Listening...';
            };
            
            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                resultDiv.innerHTML = '✅ You said: <strong>' + transcript + '</strong>';
                
                // Send the recognized text back to Streamlit
                const input = document.createElement('input');
                input.type = 'text';
                input.value = transcript;
                input.style.display = 'none';
                document.body.appendChild(input);
                
                // Trigger Streamlit's rerun
                const event = new Event('input', { bubbles: true });
                input.dispatchEvent(event);
                
                setTimeout(() => {
                    document.body.removeChild(input);
                }, 100);
            };
            
            recognition.onerror = function(event) {
                resultDiv.innerHTML = '❌ Error: ' + event.error;
                recordBtn.style.backgroundColor = '#4CAF50';
                recordBtn.innerHTML = '🎤 Click to Speak';
            };
            
            recognition.onend = function() {
                recordBtn.style.backgroundColor = '#4CAF50';
                recordBtn.innerHTML = '🎤 Click to Speak';
            };
            
            recordBtn.onclick = function() {
                if (recognition) {
                    recognition.start();
                } else {
                    resultDiv.innerHTML = '❌ Speech recognition not supported';
                }
            };
        } else {
            resultDiv.innerHTML = '❌ Your browser does not support speech recognition. Try Chrome or Edge.';
            recordBtn.disabled = true;
            recordBtn.style.backgroundColor = '#cccccc';
        }
        </script>
        '''
        
        # Display the microphone component
        components.html(microphone_html, height=200)
        
        # For capturing the result, we need a text input that gets updated
        voice_text = st.text_input("Recognized text (or type manually):", key="voice_input_browser")
        
        return voice_text if voice_text else None

browser_voice = BrowserVoiceAssistant()
