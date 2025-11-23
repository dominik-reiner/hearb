from langchain_core.tools import tool
from src.hearb.services.mcp_service import MCPService
from src.hearb.services.memory_service import MemoryService
from src.hearb.domain.models import Conversation

mcp_service = MCPService()
memory_service = MemoryService()

@tool
def get_plant_state(plant_id: str) -> str:
    """Gets the current state of the plant from the MCP."""
    plant_state = mcp_service.get_plant_state(plant_id)
    return plant_state.model_dump_json()

@tool
def save_conversation(conversation_id: str, messages_json: str):
    """Saves the conversation history."""
    # This is a placeholder for a more robust conversation saving mechanism
    # In a real scenario, you'd likely append messages rather than overwriting.
    conversation = Conversation(conversation_id=conversation_id)
    # The messages_json would need to be parsed into a list of Message objects
    memory_service.save_conversation(conversation)

@tool
def plan_steps(user_request: str) -> str:
    """Creates a plan to address the user's request."""
    # In a real implementation, this would involve a call to an LLM to generate a plan.
    return f"Plan for '{user_request}':\\n1. Get plant state.\\n2. Formulate response.\\n3. Save conversation."
