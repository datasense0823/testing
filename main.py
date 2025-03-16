from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Ensure the root path ("/") is defined
def home():
    return {"message": "I am learning FastAPI"}

@app.get("/health")  # Optional health check endpoint
def health_check():
    return {"status": "healthy"}