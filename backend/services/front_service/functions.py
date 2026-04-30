import requests

def send_message(userInput):
    url = "http://localhost:1350"

    response = requests.post( 
        url,
        json={"message": userInput}
    )

    return response.json()

