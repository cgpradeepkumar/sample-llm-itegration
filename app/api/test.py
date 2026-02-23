from fastapi import APIRouter, HTTPException

from app.service.gemini import run_query

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