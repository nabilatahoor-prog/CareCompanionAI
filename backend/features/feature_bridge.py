import streamlit as st
import base64

def render_prescription_scanner():
    st.markdown("## 📋 Prescription Scanner")
    st.markdown("*Upload a prescription to automatically extract medicines*")
    uploaded_file = st.file_uploader("Upload Prescription Image", type=["jpg", "jpeg", "png", "bmp"])
    if uploaded_file:
        st.image(uploaded_file, caption="Your Prescription", use_column_width=True)
    if st.button("🔍 Scan Prescription", type="primary", use_container_width=True):
        if not uploaded_file:
            st.warning("Please upload a prescription image first.")
        else:
            with st.spinner("Scanning..."):
                try:
                    img_b64 = base64.b64encode(uploaded_file.read()).decode()
                    from backend.scanner.prescription_scanner import scanner
                    result = scanner.scan_prescription(img_b64)
                    st.success(f"✅ Found {result['total_medicines']} medicine(s)!")
                    for i, med in enumerate(result["medicines"]):
                        with st.expander(f"💊 {med['name']}", expanded=True):
                            c1, c2, c3 = st.columns(3)
                            c1.metric("Dosage", med["dosage"])
                            c2.metric("Frequency", med["frequency"])
                            c3.metric("Timing", med["timing"])
                            if st.button("➕ Add to My Medicines", key=f"add_{i}"):
                                if "medicines_list" not in st.session_state:
                                    st.session_state.medicines_list = []
                                st.session_state.medicines_list.append(med)
                                st.success(f"{med['name']} added!")
                    with st.expander("📄 Raw OCR Text"):
                        st.text(result["raw_text"])
                except ImportError:
                    st.warning("⚠️ Tesseract not installed.")
                    st.markdown("[Download Tesseract here](https://github.com/UB-Mannheim/tesseract/wiki)")

def render_voice_assistant(gemini_chat_fn=None):
    st.markdown("## 🎙️ Voice Assistant")
    languages = {
        "English": "en", "Hindi (हिंदी)": "hi", "Telugu (తెలుగు)": "te",
        "Tamil (தமிழ்)": "ta", "Kannada (ಕನ್ನಡ)": "kn",
        "Marathi (मराठी)": "mr", "Bengali (বাংলা)": "bn", "Gujarati (ગુજрાতী)": "gu"
    }
    col1, col2 = st.columns([2, 1])
    with col1:
        selected_lang = st.selectbox("🌐 Your Language", list(languages.keys()))
    with col2:
        st.metric("Code", languages[selected_lang])
    st.info("💡 Describe symptoms, ask about medicines, or say 'book appointment'")
    col_mic, col_type = st.columns(2)
    with col_mic:
        if st.button("🎤 Start Speaking", use_container_width=True, type="primary"):
            with st.spinner(f"Listening in {selected_lang}..."):
                try:
                    from backend.voice.voice_assistant import voice_assistant
                    voice_assistant.set_language(selected_lang.split(" ")[0].lower())
                    result = voice_assistant.listen()
                    if "error" in result:
                        st.error(f"❌ {result['error']}")
                    else:
                        st.success(f"✅ Heard: {result['original']}")
                        if result["lang"] != "en":
                            st.info(f"🔄 In English: {result['english']}")
                        st.session_state["last_voice_input"] = result
                        if gemini_chat_fn:
                            resp = gemini_chat_fn(result["english"])
                            st.session_state["last_voice_response"] = resp
                            st.session_state["voice_lang"] = languages[selected_lang]
                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("Fix: pip install pipwin then pipwin install pyaudio")
    with col_type:
        typed = st.text_input("⌨️ Or type here:")
        if st.button("Send ➤", use_container_width=True):
            if typed and gemini_chat_fn:
                resp = gemini_chat_fn(typed)
                st.session_state["last_voice_response"] = resp
                st.session_state["voice_lang"] = languages[selected_lang]
    if "last_voice_response" in st.session_state:
        st.markdown("### 🤖 Gemini Says:")
        resp_text = st.session_state["last_voice_response"]
        st.markdown(f"""
        <div style="background:#1e1e3f;border-radius:12px;padding:16px;
                    border-left:4px solid #9c6cfe;color:white;">
            {resp_text}
        </div>""", unsafe_allow_html=True)
        if st.button("🔊 Read Aloud"):
            try:
                from backend.voice.voice_assistant import voice_assistant
                lang_code = st.session_state.get("voice_lang", "en")
                voice_assistant.speak(resp_text, lang=lang_code)
                st.success("Done!")
            except Exception as e:
                st.error(f"TTS error: {e}")
        keywords = ["appointment", "book", "schedule", "doctor", "consult"]
        if any(k in resp_text.lower() for k in keywords):
            st.markdown("---")
            st.markdown("### 📅 Book this appointment?")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🟢 Yes, Book!", use_container_width=True, type="primary"):
                    st.success("Redirecting to Appointments...")
                    st.session_state["auto_book"] = True
            with c2:
                if st.button("🔴 No, Cancel", use_container_width=True):
                    st.info("Cancelled.")

def render_language_settings():
    st.markdown("## 🌐 Language Settings")
    languages = {
        "English": "en", "Hindi (हिंदी)": "hi", "Telugu (తెలుగు)": "te",
        "Tamil (தமிழ்)": "ta", "Kannada (ಕನ್ನಡ)": "kn",
        "Marathi (मराठी)": "mr", "Bengali (বাংলা)": "bn", "Gujarati (ગુজрాతী)": "gu"
    }
    current = st.session_state.get("app_language", "English")
    idx = list(languages.keys()).index(current) if current in languages else 0
    selected = st.selectbox("App Language", list(languages.keys()), index=idx)
    if st.button("💾 Save", type="primary"):
        st.session_state["app_language"] = selected
        st.session_state["app_language_code"] = languages[selected]
        st.success(f"✅ Language set to {selected}")
        st.rerun()
