from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str
    k: Optional[int] = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]