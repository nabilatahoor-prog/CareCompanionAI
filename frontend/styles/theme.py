import streamlit as st

def load_theme():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        section[data-testid="stSidebar"] {
            background: linear-gradient(135deg, #ffffff 0%, #e8ecf1 100%) !important;
        }
        
        section[data-testid="stSidebar"] * {
            color: #1a1a2e !important;
        }
        
        section[data-testid="stSidebar"] h1 {
            color: #1a1a2e !important;
            font-size: 24px !important;
        }
        
        section[data-testid="stSidebar"] .stButton button {
            background: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%) !important;
            color: white !important;
            border-radius: 10px !important;
            padding: 10px 15px !important;
            width: 100% !important;
            margin: 5px 0 !important;
            text-align: center !important;
            font-weight: 600 !important;
            border: none !important;
            cursor: pointer !important;
        }
        
        section[data-testid="stSidebar"] .stButton button:hover {
            background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%) !important;
            transform: scale(1.02);
        }
        
        .stMetric {
            background: white;
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        h1, h2, h3 {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)
