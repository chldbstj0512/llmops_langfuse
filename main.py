#fastapi
from fastapi import FastAPI
from pydantic import BaseModel
import time

from llm_client import call_llm
from logger_langfuse import log_llm_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    prompt_version: str = "v1"

class ChatResponse(BaseModel):
    reply: str
    model: str
    latency_ms: float
    total_tokens: int

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):

    start = time.time()

    reply, model_name, total_tokens = call_llm(req.message, req.prompt_version)

    latency_ms = (time.time() - start) * 1000

    # logger.py 용 로그 기록
    '''log_llm_response(
        prompt=req.message,
        prompt_version=req.prompt_version,
        model=model_name,
        latency_ms=latency_ms,
        total_tokens=total_tokens,
    )'''
    
    log_llm_response(
        prompt=req.message,
        reply=reply,
        prompt_version=req.prompt_version,
        model=model_name,
        latency_ms=latency_ms,
        total_tokens=total_tokens
    )

    return ChatResponse(
        reply=reply,
        model=model_name,
        latency_ms=latency_ms,
        total_tokens=total_tokens
    )
