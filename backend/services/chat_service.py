from fastapi import HTTPException
from backend.models.chat_models import ChatMessage
from backend.services.storage_service import (
    load_history,
    save_history,
    load_summary,
    load_users,
)


def chat_user(data: ChatMessage) -> dict:
    emotion = "sadness"
    response = "Gracias por compartir esto"
    timestamp = data.timestamp.isoformat()

    history = load_history(data.user_id)
    history.append(
        {
            "message": data.message,
            "response": response,
            "emotion": emotion,
            "timestamp": timestamp,
        }
    )
    save_history(data.user_id, history)

    return {"response": response, "emotion": emotion, "timestamp": timestamp}


def get_history(user_id: str) -> dict:
    history = load_history(user_id)
    return {"history": history}


def get_summary(user_id: str) -> dict:
    summary = load_summary(user_id)
    if summary is None:
        raise HTTPException(status_code=404, detail="Summary file not found")
    return {"summary": summary}


def login(credentials: dict) -> dict:
    try:
        users = load_users()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Users file not found")

    for user in users:
        if user.get("username") == credentials.get("username") and user.get("password") == credentials.get("password"):
            return {"access_token": "your_access_token"}

    raise HTTPException(status_code=401, detail="Invalid credentials")
