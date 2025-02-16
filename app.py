print("Importing generate_letter from openai_integration")
from fastapi import FastAPI
from openai_integration import generate_letter

app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/generate-letter/")
def create_letter(prompt: str):
    letter = generate_letter(prompt)
    return {"letter": letter}

