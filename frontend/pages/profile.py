import streamlit as st

def show():
    st.title("👤 My Profile")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        uploaded_file = st.file_uploader("📸 Profile Picture", type=['png', 'jpg', 'jpeg'])
        if uploaded_file:
            st.image(uploaded_file, width=120)
        else:
            st.image("https://img.icons8.com/color/96/user.png", width=120)
    
    with col2:
        st.subheader("John Doe")
        st.write("📧 john.doe@email.com")
        st.write("🎂 Age: 65")
        st.write("🩸 Blood Type: A+")
        st.write("⚠️ Allergies: Penicillin, Peanuts")
        st.write("📍 Location: New York, NY")
    
    st.divider()
    with st.form("edit_profile"):
        st.subheader("✏️ Edit Profile")
        name = st.text_input("Full Name", "John Doe")
        age = st.number_input("Age", 18, 120, 65)
        email = st.text_input("Email", "john@email.com")
        blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        allergies = st.text_area("Allergies", "Penicillin, Peanuts")
        
        if st.form_submit_button("Update Profile", type="primary"):
            st.success("Profile updated successfully!")
