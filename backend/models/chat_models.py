from pydantic import BaseModel
from datetime import datetime


class ChatMessage(BaseModel):
    user_id: str
    message: str
    timestamp: datetime

class ChatResponse(BaseModel):
    response: str
    emotion: str
    timestamp: str