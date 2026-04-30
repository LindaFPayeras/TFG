from fastapi import APIRouter
from datetime import datetime

# Schemas (Pydantic)
from backend.models.chat_models import ChatMessage
from backend.models.auth_models import LoginRequest
from backend.models.history_models import UserData

# Casos de uso / servicios
from backend.services.chat_service.chat_service import chat_user
from backend.services.summary_service.summary_service import get_report
from backend.services.auth_service.login_user import login_user
from backend.services.data_service.data_service import save_user_data

router = APIRouter()

@router.post("/chat") # Los mensajes en si, contenido
def chat(data: ChatMessage):
    return chat_user(data)


@router.get("/report/{user_id}") # Para hacer el resumen del terapéuta
def report(user_id: str, start: str, end: str):
    from_date = datetime.fromisoformat(start)
    to_date = datetime.fromisoformat(end)
    return get_report(user_id, from_date, to_date)


@router.get("/data/{user_id}") 
def messageHistory(user_id: str, data: dict):
    #TODO: Queremos el historial de mensajes
    pass

@router.post("/auth/login")
def login(credentials: LoginRequest): 
    return login_user(credentials)

# @router.post("/login")
# def login_route(credentials: dict):
#     return login(credentials)
