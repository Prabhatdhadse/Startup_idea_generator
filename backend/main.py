import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Startup Idea Generator API is running with Gemini!"}


@app.post("/generate")
async def generate_idea(request: Request):
    data = await request.json()
    keyword = data.get("keyword", "").strip()

    if not keyword:
        return {"idea": "Please enter a keyword!"}

    prompt = f"Generate 3 creative and realistic startup ideas based on the keyword '{keyword}'. Each idea should include a short name, concept, and target audience."

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)

        idea_text = response.text.strip() if hasattr(response, "text") else "No response text found."
        return {"idea": idea_text}

    except Exception as e:
        return {"idea": f"Error generating idea: {str(e)}"}



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
