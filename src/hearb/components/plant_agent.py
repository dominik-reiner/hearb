from langgraph.graph import StateGraph
from src.hearb.components.agent_state import AgentState

# Define the workflow
workflow = StateGraph(AgentState)

# TODO: Define the nodes and edges for the plant_agent graph

# Compile the graph
plant_agent = workflow.compile()
