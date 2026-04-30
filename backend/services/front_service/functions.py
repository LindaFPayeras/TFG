import requests
from config import API_URL

def send_message(userInput):

    response = requests.post( 
        f"{API_URL}/chat",
        json={"message": userInput}
    )

    return response.json()

def load_history(userId):
    response = requests.post(
        f"{API_URL}/data/{userId}",
        json={
            "user_id": userId
        }
    )
    return response.json()