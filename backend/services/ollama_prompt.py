from ollama import chat
import os

SYSTEM_PROMPT = os.open("system_prompt.txt", "r", encoding="utf-8").read()

def chat_user(data: dict) -> dict:
    response = chat("emotional-support", data["message"], system=SYSTEM_PROMPT)
    return response