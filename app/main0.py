from fastapi import FastAPI
from pydantic import BaseModel

from app.chatbot import generate_response


app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "DPDP Chatbot API Running"
    }


@app.post("/chat")
def chat(request: QueryRequest):

    response = generate_response(
        request.query
    )

    return response

@app.get("/test-gemini")
def test_gemini():

    try:

        from google import genai
        import os

        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents="Hello"
        )

        return {
            "response": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }