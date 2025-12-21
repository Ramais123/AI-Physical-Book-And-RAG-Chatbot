import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key present: {'Yes' if api_key else 'No'}")
print(f"Key starts with: {api_key[:10] if api_key else 'N/A'}...")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        print("✅ Gemini client created successfully")
        
        # Test simple prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents="Say hello"
        )
        print(f"✅ Gemini test response: {response.text[:50]}...")
    except Exception as e:
        print(f"❌ Gemini error: {type(e).__name__}: {str(e)}")
else:
    print("❌ No API key found in .env file")
