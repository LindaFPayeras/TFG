from fastapi import HTTPException
from backend.models.chat_models import ChatMessage
from backend.services.storage_service import (
    load_history,
    save_history,
    load_summary,
    load_users,
)

from transformers import pipeline
#from ollama_prompt import chat_user as ollama_chat_user

classifier = None

def get_classifier():
    global classifier
    if classifier is None:
        classifier = pipeline(
            "text-classification",
            model="ayoubkirouane/BERT-Emotions-Classifier",
            return_all_scores=True
        )
    return classifier

def chat_user(data: ChatMessage) -> dict:
    classifier_instance = get_classifier()
    results = classifier_instance(data.message)[0]

    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True) 
    emotion = sorted_results[0]['label'] # Devuelve la label con más puntuación tras ordenarlas

    emotion = "prueba_emocion"  # Simulación de emoción, reemplaza con emotion real cuando esté disponible

    # response = ollama_chat_user({"message": data.message})
    response = "This is a simulated response."
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

