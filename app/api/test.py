from fastapi import APIRouter, HTTPException

from app.service.gemini_v1 import run_query
from app.service.gemini_v2 import run_query as run_query_v2
from app.service.vertexai import run_query as run_query_v3

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def test():
    return "Hello World!"

@router.get("/{query}")
def execute_query(query: str):
    response = run_query(query)

    if not response:
        raise HTTPException(status_code=404, detail=f"Failed to generate response.")
    
    return {"response": response}

@router.get("/v2/{query}")
def execute_query_v2(query: str):
    response = run_query_v2(query)

    if not response:
        raise HTTPException(status_code=404, detail=f"Failed to generate response.")
    
    return {"response": response}


@router.get("/v3/{query}")
def execute_query_v3(query: str):
    response = run_query_v3(query)

    if not response:
        raise HTTPException(status_code=404, detail=f"Failed to generate response.")
    
    return {"response": response}