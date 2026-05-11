import json
import jwt
from datetime import datetime, timedelta
from pathlib import Path
import os
from fastapi import HTTPException

SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
ALGORITHM = "HS256"
USERS_FILE = Path(__file__).with_name("users.json")
SIGNING_KEY = jwt.jwk_from_dict({
    "kty": "oct",
    "k": jwt.utils.b64encode(SECRET_KEY.encode("utf-8")),
})


def load_users():
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data

    return data.get("users", [])

def create_token(user_id:str):
    payload = {
        "user_id": user_id,
        "exp": int((datetime.utcnow() + timedelta(hours=2)).timestamp())
    }

    token = jwt.JWT().encode(payload, SIGNING_KEY, alg=ALGORITHM)

    return token


def login_user(credentials):
    users = load_users()

    user = next(
        (u for u in users if u["user_id"] == credentials.user_id),
        None
    )

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user["password"] != credentials.password:
        raise HTTPException(status_code=401, detail="Password incorrecta")

    token = create_token(user["user_id"])
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user["user_id"],
        "user_type": user["user_type"]
    }

