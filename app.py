from fastapi import FastAPI

app = FastAPI()


@app.get("/spinnaker-poc/healthz")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.get("/spinnaker-poc/main")
def main():
    """Main endpoint"""
    return {"sample-service": "Service is live and working fine"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
