from src.hearb.domain.models import Conversation, Message
import os
from typing import Optional

class MemoryService:
    """Manages reading and writing conversation history to Markdown files."""
    def __init__(self, memory_dir: str = "memory"):
        self.memory_dir = memory_dir
        if not os.path.exists(self.memory_dir):
            os.makedirs(self.memory_dir)

    def get_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Retrieves a conversation from a Markdown file."""
        filepath = os.path.join(self.memory_dir, f"{conversation_id}.md")
        if not os.path.exists(filepath):
            return None

        with open(filepath, "r") as f:
            content = f.read()

        messages = []
        # Simple parsing logic, can be made more robust
        for line in content.split("\n---\n"):
            if line.strip():
                parts = line.split(":", 1)
                sender = parts[0].strip().lower()
                message_content = parts[1].strip()
                messages.append(Message(sender=sender, content=message_content, timestamp="")) # Timestamp can be added

        return Conversation(conversation_id=conversation_id, messages=messages)

    def save_conversation(self, conversation: Conversation):
        """Saves a conversation to a Markdown file."""
        filepath = os.path.join(self.memory_dir, f"{conversation.conversation_id}.md")
        with open(filepath, "w") as f:
            for message in conversation.messages:
                f.write(f"**{message.sender.capitalize()}**: {message.content}\n\n---\n")
