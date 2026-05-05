import json
from datetime import datetime
from backend.services.data_service.storage_service import load_history, load_patients


def get_user_history(user_id: str):
    history = load_history(user_id)
    return history

def get_patient_list(therapist_id: str):
    data = load_patients()
    for therapist in data:
        if therapist["user_id"] == therapist_id:
            return therapist["patient_list"]
    return []