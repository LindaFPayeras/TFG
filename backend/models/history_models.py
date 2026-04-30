from pydantic import BaseModel
from typing import List
from datetime import datetime

class MessageEntry(BaseModel):
    message: str
    timestamp: datetime

class UserData(BaseModel):
    messages: List[MessageEntry]

    
