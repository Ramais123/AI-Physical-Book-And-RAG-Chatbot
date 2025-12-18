import google.generativeai as genai

# Direct API key yahan daalo
API_KEY = "AIzaSyD..."  # APNI KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Hello, are you working?")
print("✅ Gemini Response:", response.text)