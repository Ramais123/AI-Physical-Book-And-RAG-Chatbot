from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = FastAPI(title="Physical AI Book Assistant API")

# CORS setup for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class QuestionRequest(BaseModel):
    question: str
    selected_text: str = ""
    user_background: Optional[str] = "beginner"

class PersonalizeRequest(BaseModel):
    text: str
    level: str = "beginner"

class TranslationRequest(BaseModel):
    text: str
    target_language: str = "urdu"

# Initialize Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("⚠️ Warning: GEMINI_API_KEY not found in .env")
    client = None
else:
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("✅ Gemini API configured")

# Simple book knowledge base (for demo)
BOOK_KNOWLEDGE = {
    "ros2": "ROS 2 (Robot Operating System 2) is middleware for robot software development.",
    "gazebo": "Gazebo is a physics simulation environment for robotics.",
    "isaac": "NVIDIA Isaac provides AI capabilities for robotics perception.",
    "vla": "Vision-Language-Action models combine multiple AI modalities."
}

# ========== ✅ HEALTH ENDPOINT ==========

@app.get("/")
async def root():
    """Root endpoint - Welcome message"""
    return {
        "message": "🚀 Physical AI Book Assistant API",
        "status": "online",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "health": "GET /health",
            "ask": "POST /api/ask",
            "personalize": "POST /api/personalize",
            "translate": "POST /api/translate",
            "docs": "GET /docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for frontend"""
    gemini_status = "configured" if GEMINI_API_KEY else "not_configured"
    
    return {
        "status": "healthy",
        "service": "Physical AI Book Assistant",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "gemini_api": gemini_status,
        "endpoints": {
            "root": "GET /",
            "health": "GET /health",
            "ask_question": "POST /api/ask",
            "personalize": "POST /api/personalize",
            "translate": "POST /api/translate"
        }
    }

@app.get("/test")
async def test_endpoint():
    """Test endpoint for quick checks"""
    return {
        "message": "✅ Backend is working!",
        "test": "successful",
        "timestamp": datetime.now().isoformat()
    }

# ========== EXISTING ENDPOINTS ==========

@app.post("/api/ask")
async def ask_question(request: QuestionRequest):
    """Main RAG endpoint with text selection"""
    if not client:
        # Mock response if Gemini not configured
        return {
            "answer": f"🤖 Mock Response to: '{request.question}'\n\nGemini API not configured. Please add GEMINI_API_KEY to .env file.",
            "context_used": bool(request.selected_text),
            "question": request.question,
            "mode": "mock",
            "timestamp": datetime.now().isoformat()
        }
    
    try:
        # Use selected text if provided, else use book knowledge
        context = request.selected_text if request.selected_text else "\n".join(BOOK_KNOWLEDGE.values())
        
        prompt = f"""You are a helpful teaching assistant for Physical AI & Humanoid Robotics.

CONTEXT FROM TEXTBOOK:
{context}

QUESTION: {request.question}

USER BACKGROUND: {request.user_background}

Answer based only on the textbook context above.
If the answer isn't in the context, say "I don't have enough information in the textbook."
"""
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        
        return {
            "answer": response.text,
            "context_used": "selected_text" if request.selected_text else "full_book",
            "question": request.question,
            "context_length": len(context),
            "timestamp": datetime.now().isoformat(),
            "mode": "gemini"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/personalize")
async def personalize_content(request: PersonalizeRequest):
    """Personalize content based on user level"""
    if not client:
        raise HTTPException(status_code=500, detail="Gemini API not configured")
    
    try:
        prompt = f"""Rewrite this technical robotics content for a {request.level} level student.

Original text:
{request.text}

Rewritten version ({request.level} level):
"""
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        
        return {"personalized_text": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/translate")
async def translate_content(request: TranslationRequest):
    """Translate content to Urdu"""
    if not client:
        raise HTTPException(status_code=500, detail="Gemini API not configured")
    
    try:
        prompt = f"""Translate this technical English text to Urdu.
Keep technical robotics terms in English but explain them in Urdu in parentheses.

English text:
{request.text}

Urdu translation:
"""
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        
        return {"translated_text": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os


    print("=" * 60)
    print("🚀 Starting Physical AI Book Assistant API")
    print("📡 URL: http://localhost:8000")
    print("🏥 Health: http://localhost:8000/health")
    print("🤖 Ask: http://localhost:8000/api/ask")
    print("📚 Docs: http://localhost:8000/docs")
    print("⚙️ Gemini API:", "✅ Configured" if GEMINI_API_KEY else "❌ Not configured")
    print("=" * 60)
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=8000)