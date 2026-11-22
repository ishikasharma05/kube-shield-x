from fastapi import FastAPI
import os, socket

app = FastAPI(title="security-api")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {
        "service": "security-api",
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "pod": socket.gethostname(),
    }