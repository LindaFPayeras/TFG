import json
import bcrypt

def find_user(username):
    with open("users.json", "r") as f:
        users = json.load(f)
    for user in users:
        if user["username"] == username:
            return user
    return None

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

