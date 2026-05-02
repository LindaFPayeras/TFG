import requests
from backend.front_service.config import API_URL

def send_message(user_id, user_input):

    response = requests.post( 
        f"{API_URL}/chat",
        json={
            "user_id": user_id,
            "message": user_input
        }
    )

    return response.json()

def load_history(user_id):
    response = requests.get(
        f"{API_URL}/data/{user_id}",
    )
    data = response.json()

    if isinstance(data, list):
        return data

    return []
