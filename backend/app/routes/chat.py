from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.services.llm_agent import get_ai_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat_with_agent(req: ChatRequest):
    reply = await get_ai_response(req.message)
    return {"reply": reply}