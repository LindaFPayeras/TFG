import os
from datetime import datetime
import json
from collections import Counter

def get_messages_in_range(messages, from_date, to_date):
    filtered = []

    for msg in messages:
        ts = datetime.fromisoformat(msg["timestamp"])

        if from_date <= ts <= to_date:
            filtered.append(msg)

    return filtered

def get_top_emotions(messages):
    emotions = [
        msg["emotion"]
        for msg in messages
        if msg["role"] == "user" and msg["emotion"] is not None
    ]

    counter = Counter(emotions)

    return [e[0] for e in counter.most_common(3)]
    
def format_history_for_summary(messages):
    formatted = ""

    for msg in messages:
        ts = datetime.fromisoformat(msg["timestamp"])
        ts_str = ts.strftime("%H:%M, %d/%m/%Y")
        role = "Paciente" if msg["role"] == "user" else "Asistente"
        formatted += f"[{ts_str}] {role}: {msg['content']}\n"

    return formatted

def generate_summary(messages):
    history_text = format_history_for_summary(messages)

    prompt = f"""
        Eres un asistente que analiza conversaciones entre un paciente y un sistema de apoyo emocional.

        Genera un resumen claro, objetivo y estructurado del estado del paciente.

        No des consejos.
        No inventes información.
        Describe emociones, situación y evolución.

        Conversación:
        {history_text}
    """

    return call_ollama(prompt)  # o tu función de ollama

def get_report(user_id: str, from_date, to_date):

    history = format_history_for_summary(user_id)

    messages = get_messages_in_range(history, from_date, to_date)

    if not messages:
        return {
            "summary": "No hay datos en este periodo",
            "top_emotions": [],
            "num_messages": 0
        }

    top_emotions = get_top_emotions(messages)

    summary = generate_summary(messages)

    return {
        "summary": summary,
        "top_emotions": top_emotions,
        "num_messages": len(messages)
    }