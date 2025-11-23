from src.hearb.domain.models import PlantState
import datetime

class MCPService:
    """A mock service to simulate interactions with the MCP server."""

    def get_plant_state(self, plant_id: str) -> PlantState:
        """Simulates fetching the current state of a plant."""
        # In a real implementation, this would make an API call to the MCP server.
        return PlantState(
            plant_id=plant_id,
            name="Ficus",
            moisture=0.5,
            temperature=22.0,
            humidity=0.6,
            last_watered=datetime.datetime.now().isoformat()
        )
