# Hiring-assistant
Overview :
This is hiring assistant, a chatbot who helps interviewer in the process. It can generate questions according to specific candidate.
Candidate can start initial interview process via this chatbot and it will help recruiter to filter out candidates.

Installation instruction :
This chatbot is built using following libraries,
1. Streamlit for creating front end using python.
2. Fast api for backend and integrating OpenAI API.
3. OpenAI api for the use of GPT3/4.

To run this application install above libraries and run,
'uvicorn hiring_assistant:app --reload' and after that run,
'streamlit run streamlit_app.py'.

Usage guide:
Enter full name, years of experience and select your tech stack according to your skills.
After that you will get questions according to your skills, guve answers and submit it.
