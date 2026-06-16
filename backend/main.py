from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title="Choose Your Own Adventrue Game API",
    description="api to generate cool stories",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Adding this middleware here, called CORS (Cross-Origin Resource Sharing)
# So we´re allowed to enable certain origin. So certain URLs to interact with our backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"], # Like GET(retrieving data), POST(making date), PUT(updating data)
    allow_headers=["*"], # additional information we can send with the request
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)