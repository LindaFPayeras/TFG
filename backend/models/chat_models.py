from pydantic import BaseModel
from datetime import datetime


class ChatMessage(BaseModel):
    user_id: str
    message: str
    timestamp: datetime
