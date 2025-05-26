"""State definitions.

State is the interface between the graph and end user as well as the
data model used internally by the graph.
"""

import operator
from dataclasses import dataclass, field
from typing import Annotated, Any, Dict, List, Optional
from pydantic import BaseModel
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages

def add_results(existing_results: List[Dict[str, Any]], new_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Custom reducer for search results that only appends unique results based on URL.
    
    Args:
        existing_results: The existing list of search results
        new_results: The new list of search results to add
        
    Returns:
        A new list containing both existing results and new unique results
    """
    if not new_results:
        return existing_results

    # Create a set of existing URLs for faster lookup
    existing_urls = {result.get("url", "") for result in existing_results}
    

    # Only append results with URLs not already in the existing results
    result = existing_results.copy()
    for item in new_results:
        url = item.get("url", "")
        if url and url not in existing_urls:
            result.append(item)
            existing_urls.add(url)
    
    return result

@dataclass(kw_only=True)
class InputState:
    """Input state defines the interface between the graph and the user (external API)."""
    company_name: str
    company_info: str
    procurement_requirement: str

@dataclass(kw_only=True)
class ContactDetails(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None

@dataclass(kw_only=True)
class Supplier(BaseModel):
    name: str
    description: str
    standards_compliance: str
    certifications: str
    contact_details: ContactDetails = field(default_factory=ContactDetails)



@dataclass(kw_only=True)
class State(InputState):
    """A graph's State defines three main things.

    1. The structure of the data to be passed between nodes (which "channels" to read from/write to and their types)
    2. Default values for each field
    3. Reducers for the state's fields. Reducers are functions that determine how to apply updates to the state.
    See [Reducers](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) for more information.
    """

    messages: Annotated[List[BaseMessage], add_messages] = field(default_factory=list)
    """
    Messages track the primary execution state of the agent.

    Typically accumulates a pattern of:

    1. HumanMessage - user input
    2. AIMessage with .tool_calls - agent picking tool(s) to use to collect
        information
    3. ToolMessage(s) - the responses (or errors) from the executed tools

        (... repeat steps 2 and 3 as needed ...)
    4. AIMessage without .tool_calls - agent responding in unstructured
        format to the user.

    5. HumanMessage - user responds with the next conversational turn.

        (... repeat steps 2-5 as needed ... )

    Merges two lists of messages, updating existing messages by ID.

    By default, this ensures the state is "append-only", unless the
    new message has the same ID as an existing message.

    Returns:
        A new list of messages with the messages from `right` merged into `left`.
        If a message in `right` has the same ID as a message in `left`, the
        message from `right` will replace the message from `left`.
        """

    loop_step: Annotated[int, operator.add] = field(default=0)
    
    # Add info attribute to store the extracted information
    info: Optional[Dict[str, Any]] = field(default=None)

    queries: Optional[List[str]] = field(default=None) 

    search_results: Annotated[List[Dict[str, Any]], operator.add] = field(default_factory=list)

    suppliers: Annotated[List[Supplier], operator.add] = field(default_factory=list)
    # Feel free to add additional attributes to your state as needed.
    # Common examples include retrieved documents, extracted entities, API connections, etc.

@dataclass(kw_only=True)
class ResultState(BaseModel):
    """A search result."""
    search_result: Dict[str, Any]

@dataclass(kw_only=True)
class Queries(BaseModel):
    """A search result."""
    queries: List[str]

@dataclass(kw_only=True)
class SearchState(BaseModel):
    """A search query"""
    query: str




class OutputState:
    """The response object for the end user.

    This class defines the structure of the output that will be provided
    to the user after the graph's execution is complete.
    """

    info: dict[str, Any]
    """
    A dictionary containing the extracted and processed information
    based on the user's query and the graph's execution.
    This is the primary output of the enrichment process.
    """
