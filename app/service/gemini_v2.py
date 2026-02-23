import logging
from google import genai
from app.core.config import settings

logger = logging.getLogger(__name__)
client = genai.Client(api_key=settings.GEMINI_API_KEY)

def run_query(query: str):
    try:
        logger.info(f"running query: {query}")
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL_ID,
            contents=query)   
        return response.text
    except Exception as e:
        logger.error(f"Error while running query: {e}", exc_info=True)
        raise