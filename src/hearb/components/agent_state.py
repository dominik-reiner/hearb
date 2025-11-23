from typing import List, TypedDict, Annotated
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    """
    Represents the shared state of the LangGraph agents.
    It passes data between the nodes of the graph.
    """
    messages: Annotated[List[BaseMessage], operator.add]
    # Other state variables like plan, intermediate steps, etc., can be added here.
