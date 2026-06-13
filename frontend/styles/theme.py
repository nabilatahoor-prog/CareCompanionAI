import streamlit as st

def load_theme():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%) !important;
            border-right: 2px solid #818cf8 !important;
        }
        
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        [data-testid="stSidebar"] h1 {
            color: white !important;
            font-size: 24px !important;
            font-weight: bold !important;
            text-align: center !important;
            border-bottom: 2px solid #818cf8 !important;
            padding-bottom: 10px !important;
        }
        
        [data-testid="stSidebar"] .stButton button {
            background: linear-gradient(135deg, #1e1b4b 0%, #4c1d95 100%) !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 10px 15px !important;
            width: 100% !important;
            margin: 5px 0 !important;
            text-align: left !important;
            font-weight: 500 !important;
            border: 1px solid #818cf8 !important;
        }
        
        [data-testid="stSidebar"] .stButton button:hover {
            background: linear-gradient(135deg, #312e81 0%, #6d28d9 100%) !important;
            transform: translateX(3px);
            border-color: #c4b5fd !important;
        }
        
        [data-testid="stSidebar"] hr {
            border-color: #818cf8 !important;
        }
        
        .stMetric {
            background: white !important;
            border-radius: 15px !important;
            padding: 15px !important;
            border-left: 5px solid #818cf8 !important;
        }
        
        .stMetric label {
            color: #4c1d95 !important;
            font-weight: bold !important;
        }
        
        h1, h2, h3 {
            color: white !important;
        }
        
        .stDataFrame {
            background: white !important;
            border-radius: 10px !important;
        }
        </style>
    """, unsafe_allow_html=True)
