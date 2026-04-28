import json
from datetime import datetime

def get_report(user_id: str) -> dict:
    with open(f"data/history/history_{user_id}.json", "r") as f:
        return json.load(f)
    
def format_history_for_summary(messages: dict):
    formatted = ""

    for msg in messages:
        ts = datetime.fromisoformat(msg["timestamp"])
        ts_str = ts.strftime("%H:%M, %d/%m/%Y")
        role = "Paciente" if msg["role"] == "user" else "Asistente"
        formatted += f"[{ts_str}] {role}: {msg['content']}\n"

    return formatted