from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    userInput: str

class BulkChatRequest(BaseModel):
    inputs: List[str]