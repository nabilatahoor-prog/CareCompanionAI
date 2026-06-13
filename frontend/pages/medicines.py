import streamlit as st

def show():
    st.title("💊 Medicines")
    
    st.subheader("🌅 Morning (8:00 AM)")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.checkbox("Aspirin 81mg", value=True)
    with col2:
        st.success("Taken")
    
    st.checkbox("Vitamin D 1000 IU")
    
    st.subheader("☀️ Afternoon (1:00 PM)")
    st.checkbox("Blood Pressure Medication")
    
    st.subheader("🌙 Evening (8:00 PM)")
    st.checkbox("Cholesterol Medicine")
    
    if st.button("✓ Mark All as Taken", type="primary"):
        st.success("All medications marked as taken for today!")
        st.balloons()
