import uvicorn
from fastapi import FastAPI

from app.core.logging_config import setup_logging
from app.api.test import router as test_router

setup_logging()

app = FastAPI()

app.include_router(test_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)