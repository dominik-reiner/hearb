from pydantic import BaseModel
from typing import List, Dict, Any

class PlantState(BaseModel):
    """Represents the current state of a plant."""
    plant_id: str
    name: str
    moisture: float
    temperature: float
    humidity: float
    last_watered: str

class Message(BaseModel):
    """Represents a single message in a conversation."""
    sender: str  # 'user' or 'agent'
    content: str
    timestamp: str

class Conversation(BaseModel):
    """Represents a conversation history."""
    conversation_id: str
    messages: List[Message] = []
