from pathlib import Path

from ollama import chat

SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "backend" / "services" / "system_prompt.txt"
SYSTEM_PROMPT = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def ollama_chat_user(data: dict) -> dict:
    try:
        response = chat(
            model="emotional-support",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": data["message"]},
            ],
        )
        return {"response": response["message"]["content"]}
    except ConnectionError:
        return {
            "response": "No se pudo conectar con Ollama. Asegurate de que el servicio este ejecutandose y el modelo 'emotional-support' este disponible."
        }
