from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

# Initialize FastAPI app
app = FastAPI()

# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"] #Save api key in enviroment variables.

# Define request model
class CandidateInfo(BaseModel):
    name: str
    experience: int  # Years of experience
    tech_stack: str  # e.g., Python, Java, React

# Function to generate interview questions
def generate_questions(tech_stack: str):
    try:
        prompt = f"Generate 3 interview questions for a candidate skilled in {tech_stack}."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"].split("\n")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API endpoint to handle candidate info and return questions
@app.post("/generate-questions/")
def get_questions(candidate: CandidateInfo):
    questions = generate_questions(candidate.tech_stack)
    return {"name": candidate.name, "questions": questions}

# Run the app using: uvicorn filename:app --reload
