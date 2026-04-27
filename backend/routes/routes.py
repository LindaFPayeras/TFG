from fastapi import APIRouter
from backend.models.chat_models import ChatMessage
from backend.services.chat_service import chat_user
from backend.services.summary_service import get_report
from datetime import datetime

router = APIRouter()


@router.post("/chat")
def chat(data: ChatMessage):
    return chat_user(data)


@router.get("/report/{user_id}")
def report(user_id: str, start: str, end: str):
    from_date = datetime.fromisoformat(start)
    to_date = datetime.fromisoformat(end)

    return get_report(user_id, from_date, to_date)

# @router.post("/login")
# def login_route(credentials: dict):
#     return login(credentials)
