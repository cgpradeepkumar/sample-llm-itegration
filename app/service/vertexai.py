import logging
from google import genai
from google.oauth2 import service_account
from app.core.config import settings

logger = logging.getLogger(__name__)

_client = None

def get_gemini_client():

    global _client

    if _client is None:
        
        cred = service_account.Credentials.from_service_account_file(
            settings.GOOGLE_APPLICATION_CREDENTIALS,
            scopes=settings.SCOPES
        )

        _client = genai.Client(
            vertexai=True,
            project=settings.GOOGLE_CLOUD_PROJECT,
            location=settings.GOOGLE_CLOUD_LOCATION,
            credentials=cred
        )
    return _client

def run_query(query: str):
    try:
        logger.info(f"running query: {query}")
        response = get_gemini_client().models.generate_content(
            model=settings.GEMINI_MODEL_ID,
            contents=query)   
        return response.text
    except Exception as e:
        logger.error(f"Error while running query: {e}", exc_info=True)
        raise