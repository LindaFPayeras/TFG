import json

def signup(username, password):
    with open("users.json", "r") as f:
        users = json.load(f)
    
    if any(user["username"] == username for user in users):
        return "Username already exists"
    
    users.append({"username": username, "password": password, "role": "user"})
    
    with open("users.json", "w") as f:
        json.dump(users, f)
    
    return "Signup successful"

