from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os

# Import main agent
from agents.main_agent import handle_user_request

# Load environment variables
load_dotenv()

app = FastAPI()

# ==============================
# CORS (for frontend)
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# ROOT ENDPOINT (SERVE UI)
# ==============================
@app.get("/")
def serve_ui():
    return FileResponse("app.html")


# ==============================
# MAIN QUERY ENDPOINT
# ==============================
@app.get("/query")
def query(user_input: str = Query(..., description="User request")):
    try:
        response = handle_user_request(user_input)

        return {
            "status": "success",
            "input": user_input,
            "response": response
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ==============================
# HEALTH CHECK (for debugging)
# ==============================
@app.get("/health")
def health():
    return {"status": "ok"}


# ==============================
# RUN LOCALLY / CLOUD RUN
# ==============================
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))  # Cloud Run uses 8080
    uvicorn.run("app:app", host="0.0.0.0", port=port)