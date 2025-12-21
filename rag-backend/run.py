import uvicorn

if __name__ == "__main__":
    print("🚀 Starting Physical AI Book Assistant API")
    print("📡 URL: http://localhost:8000")
    print("🏥 Health: http://localhost:8000/health")
    
    # ✅ Correct way to run with reload
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )