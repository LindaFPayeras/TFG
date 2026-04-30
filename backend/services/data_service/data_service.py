import json
from datetime import datetime
from backend.services.data_service.storage_service import load_history


def get_user_history(user_id: str):
    history = load_history(user_id)
    return history
