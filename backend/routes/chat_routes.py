from fastapi import APIRouter
from backend.models.chat_models import ChatMessage
from backend.services.chat_service import chat_user, get_history, get_summary, login

router = APIRouter()


@router.post("/chat")
def chat(data: ChatMessage):
    return chat_user(data)


@router.get("/history/{user_id}")
def read_history(user_id: str):
    return get_history(user_id)


@router.get("/summary/{user_id}")
def read_summary(user_id: str):
    return get_summary(user_id)


@router.post("/login")
def login_route(credentials: dict):
    return login(credentials)
