from datetime import datetime
from transformers import pipeline

from backend.models.chat_models import ChatMessage
from backend.services.data_service.storage_service import load_history, save_history
from backend.services.chat_service.ollama_service import generate_response
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

def classify_emotion(text: str) -> str:
    classifier = get_classifier()
    result = classifier(text)[0]   
    return result["label"]

def format_history(history: list) -> str:
    formatted = ""

    for msg in history:
        role = "Paciente" if msg["role"] == "user" else "Asistente"
        formatted += f"{role}: {msg['content']}\n"

    return formatted

def chat_user(data: ChatMessage) -> dict:

    user_id = data.user_id
    text = data.message
    timestamp = datetime.now().isoformat()

    # 1. Clasificar emoción
    emotion = classify_emotion(text)

    # 2. Cargar historial
    history = load_history(user_id)

    # 3. Guardar mensaje usuario
    user_message = {
        "user_id": user_id,
        "role": "user",
        "content": text,
        "emotion": emotion,
        "timestamp": timestamp
    }
    history.append(user_message)

    # 4. Generar respuesta
    response = generate_response(history)

    # 5. Guardar respuesta IA
    ai_message = {
        "user_id": user_id,
        "role": "assistant",
        "content": response,
        "emotion": None,
        "timestamp": timestamp
    }
    history.append(ai_message)

    # 6. Guardar historial
    save_history(user_id, history)

    # 7. Devolver respuesta
    return {
        "response": response,
        "emotion": emotion
    }

