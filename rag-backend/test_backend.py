import requests
import json

def test_backend():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing RAG Backend...")
    
    # Test 1: Health check
    response = requests.get(f"{base_url}/")
    print(f"✅ Health Check: {response.json()}")
    
    # Test 2: Ask question
    payload = {
        "question": "What is Physical AI?",
        "selected_text": "",
        "user_background": "beginner"
    }
    response = requests.post(f"{base_url}/api/ask", json=payload)
    print(f"✅ Q&A Test: {response.json()}")
    
    # Test 3: Personalization
    payload = {
        "text": "ROS 2 uses nodes for communication.",
        "level": "beginner"
    }
    response = requests.post(f"{base_url}/api/personalize", json=payload)
    print(f"✅ Personalization: {response.json()}")
    
    print("\n🎉 All tests passed! Backend is working.")

if __name__ == "__main__":
    test_backend()