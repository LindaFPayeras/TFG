from backend.services.data_service.storage_service import load_history
from .callOllama import call_ollama
from datetime import datetime


def format_history_for_summary(messages):
    formatted_messages = []

    for msg in messages:
        ts = datetime.fromisoformat(msg["timestamp"])
        ts_str = ts.strftime("%H:%M, %d/%m/%Y")
        role = "Paciente" if msg["role"] == "user" else "Asistente"
        formatted_messages.append(f"[{ts_str}] {role}: {msg['content']}")

    return "\n".join(formatted_messages)

system_prompt = open("backend\services\summary_service\system_prompt.txt", "r", encoding="utf-8").read()
def get_report(user_id: str):
    user_history = load_history(user_id)

    if not user_history:
        return {
            "user_id": user_id,
            "summary": "No hay datos para este usuario",
            "num_messages": 0,
        }

    formatted_history = format_history_for_summary(user_history)
    prompt = f"{system_prompt}\n{formatted_history}"
    summary = call_ollama(prompt)

    return {
        "user_id": user_id,
        "summary": summary,
        "num_messages": len(user_history),
    }
