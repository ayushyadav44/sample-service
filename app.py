import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/argocd-poc/healthz")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.get("/argocd-poc/main")
def main():
    """Main endpoint"""
    return {"sample-service": "Service is live and working fine, alongwith image updater, test-2, githuv actions is working"}

@app.get("/argocd-poc/config")
def get_config():
    """Display ConfigMap parameters injected as environment variables"""
    return {
        "SERVICE_NAME": os.getenv("SERVICE_NAME", "not set"),
        "API_BASE_URL": os.getenv("API_BASE_URL", "not set"),
        "CONFIGMAP_PARAM_1": os.getenv("CONFIGMAP_PARAM_1", "not set"),
        "CONFIGMAP_PARAM_2": os.getenv("CONFIGMAP_PARAM_2", "not set"),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
