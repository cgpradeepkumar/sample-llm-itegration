import logging
import google.generativeai as genai

from app.core.config import settings

logger = logging.getLogger(__name__)

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(settings.GEMINI_MODEL_ID)

def run_query(query: str):
    try:
        logger.info(f"running query: {query}")
        response = model.generate_content(query)    
        return response.text
    except Exception as e:
        logger.error(f"Error while running query: {e}", exc_info=True)
        raise
    
