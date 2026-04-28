from pathlib import Path
from ollama import chat

SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "system_prompt.txt"
SYSTEM_PROMPT = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def generate_response(history: list) -> str:
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for msg in history:
            role = "user" if msg["role"] == "user" else "assistant"
            messages.append({
                "role": role,
                "content": msg["content"]
            })

        response = chat(
            model="llama3:latest",
            messages=messages,
        )

        return response["message"]["content"]

    except Exception as e:
        print(f"Error: {e}")
        return "No se pudo generar respuesta en este momento."