import traceback
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger=get_logger(__name__)

app=FastAPI(title='Multi AI AGENT')

class RequestState(BaseModel):
    name_of_model:str
    system_prompt:str
    messages:List[str]
    allow_search: bool

@app.post("/chat")

def chat_endpoint(request:RequestState):
    logger.info(f"Request received for model : {request.name_of_model}")

    logger.info(f"request: {request}")
    logger.info(f"model: {request.name_of_model}")
    logger.info(f"messages: {request.messages}")
    logger.info(f"system_prompt: {request.system_prompt}")
    logger.info(f"allow_search: {request.allow_search}")

    if request.name_of_model not in settings.ALLOWED_MODEL_NAMES:
        logger.warning("Invalid model name")
        raise HTTPException(status_code=400,detail='Invalid model name')

    try:
        response=get_response_from_ai_agents(
            request.name_of_model,
            request.messages,
            request.allow_search,
            request.system_prompt
        )

        logger.info(f"successfully got response from AI agent {request.name_of_model}")

        return {"response" : response}
    
    except Exception as e:
        logger.error("Exception: " + str(e))
        logger.error(traceback.format_exc())
        raise HTTPException(
        status_code=500,
        detail=str(CustomException("Failed to get AI response", error_detail=e))
    )

   

    




