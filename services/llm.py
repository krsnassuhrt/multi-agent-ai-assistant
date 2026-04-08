# services/llm.py

import requests
import google.auth
from google.auth.transport.requests import Request

# ==============================
# CONFIG
# ==============================
PROJECT_ID = "build-ai-powered-applications"
LOCATION = "global"
MODEL = "gemini-3-flash-preview"

# ==============================
# GET ACCESS TOKEN (IAM)
# ==============================
def get_access_token():
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    return credentials.token


# ==============================
# CALL GEMINI
# ==============================
def call_gemini(prompt: str):
    try:
        access_token = get_access_token()

        url = f"https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL}:generateContent"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        body = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=body)
        data = response.json()

        if "candidates" not in data:
            return f"ERROR: {data}"

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"ERROR_CALLING_GEMINI: {str(e)}"


# ==============================
# INTENT EXTRACTION USING LLM
# ==============================
def detect_intent_llm(user_input: str):
    prompt = f"""
You are an intelligent assistant.

Classify the user request into one of these categories:
- task
- calendar
- notes
- multi

If multiple actions are present, return "multi".

Only return one word.

User input:
{user_input}
"""

    result = call_gemini(prompt)

    return result.strip().lower()