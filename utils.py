import json
from turtle import st

def find_user(username):
    with open("users.json", "r") as f:
        users = json.load(f)
    for user in users:
        if user["username"] == username:
            return user
    return st.error("User not found")

def find_conversation(user_id):
    with open(f"conversations/{user_id}.json", "r") as f:
        conversations = json.load(f)
    for convo in conversations:
        if convo["user_id"] == user_id:
            return convo
    return st.error("Conversation not found")
