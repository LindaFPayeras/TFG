from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatMessage(BaseModel):
    user_id: str
    message: str
    timestamp: Optional[datetime] = None

class ChatResponse(BaseModel):
    message: str
    emotion: str
    timestamp: Optional[datetime] = None