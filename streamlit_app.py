import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/generate-questions/"

# Streamlit UI setup
st.title("🤖 TalentScout Hiring Assistant")
st.write("Welcome! Please enter your details to start the initial screening.")

# Collect candidate information
name = st.text_input("👤 Your Name")
experience = st.number_input("💼 Years of Experience", min_value=0, max_value=50, step=1)
tech_stack = st.selectbox(
    "🛠️ Select Your Tech Stack",
    ["Python", "Java", "JavaScript", "React", "Django", "C++", "Node.js"],
)

# Submit button
if st.button("Start Screening"):
    if not name or not experience or not tech_stack:
        st.error("Please fill in all the details before proceeding.")
    else:
        # Prepare data for FastAPI
        payload = {
            "name": name,
            "experience": experience,
            "tech_stack": tech_stack,
        }

        # Send request to FastAPI backend
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                data = response.json()
                st.success(f"✅ Questions generated for {name}:")
                for i, question in enumerate(data["questions"], 1):
                    st.write(f"{i}. {question}")
            else:
                st.error("❌ Error generating questions. Please try again.")
        except Exception as e:
            st.error(f"⚠️ API request failed: {str(e)}")
