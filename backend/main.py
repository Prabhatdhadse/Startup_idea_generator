import os
from dotenv import load_dotenv
import openai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Load .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # automatically read key from .env

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for security
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Startup Idea Generator API is running!"}


# @app.post("/generate")
# async def generate_idea(request: Request):
#     data = await request.json()
#     keyword = data.get("keyword", "").strip()

#     if not keyword:
#         return {"idea": "Please enter a keyword!"}

#     prompt = f"Generate a creative startup idea based on the keyword '{keyword}'."

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             max_tokens=100,
#             temperature=0.9,
#         )

#         idea = response["choices"][0]["message"]["content"].strip()
#         return {"idea": idea}

#     except Exception as e:
#         return {"idea": f"Error generating idea: {str(e)}"}

@app.post("/generate")
async def generate_idea(request: Request):
    data = await request.json()
    keyword = data.get("keyword", "")
    if not keyword:
        return {"idea": "Please enter a keyword!"}
    
    # Temporary dummy idea
    return {"idea": f"Creative startup idea for '{keyword}'."}
