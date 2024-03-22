import streamlit as st

# Define badge thresholds
BADGE_THRESHOLDS = {
    "Bronze": 100,
    "Silver": 200,
    "Gold": 300
}

def calculate_badge(points):
    for badge, threshold in BADGE_THRESHOLDS.items():
        if points >= threshold:
            return badge
    return "None"

# Initialize user points and badges
user_points = 0
user_badge = "None"

# Define background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the title and subtitle of the app
st.title("Motivational Posture Management System")
st.subheader("Patient Registration")

# Create input fields for patient information
patient_name = st.text_input("Patient Name", "")
patient_age = st.number_input("Patient Age", min_value=0, max_value=150, step=1, value=0)
patient_gender = st.radio("Gender", options=["Male", "Female", "Other"])

# Create a button for registering the patient and earning points
if st.button("Register Patient"):
    # Update user points and badge
    user_points += 50
    user_badge = calculate_badge(user_points)
    
    # Display points and badge
    st.success(f"Patient Registered Successfully! You earned 50 points.")
    st.info(f"Total Points: {user_points}")
    st.info(f"Current Badge: {user_badge}")

# Create a button for completing a task and earning points
if st.button("Complete Task"):
    # Update user points and badge
    user_points += 100
    user_badge = calculate_badge(user_points)
    
    # Display points and badge
    st.success(f"Task Completed Successfully! You earned 100 points.")
    st.info(f"Total Points: {user_points}")
    st.info(f"Current Badge: {user_badge}")
