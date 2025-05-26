import json
import asyncio
from typing import Any, Dict, List, Literal, Optional, cast

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.types import Send
from pydantic import BaseModel, Field

from enrichment_agent.prompts import MAIN_PROMPT
from enrichment_agent.configuration import Configuration
from enrichment_agent.schema import schema
from enrichment_agent.state import InputState, OutputState, Queries, SearchState, State, Supplier, ResultState
from enrichment_agent.utils import init_model, check_for_business_website


from tavily import TavilyClient

import asyncio


async def call_agent_model(
    state: State, *, config: Optional[RunnableConfig] = None
) -> Dict[str, Any]:
    """Call the agent model to generate search queries."""

    # Initialize the model
    raw_model = init_model(config)
    
    # Create a model with structured output
    structured_model = raw_model.with_structured_output(Queries)
    
    # Get the configuration
    configuration = Configuration.from_runnable_config(config)
    
    # Format the prompt
    p = MAIN_PROMPT.format(
        company_name=state.company_name,
        company_info=state.company_info,
        procurement_requirement=state.procurement_requirement,
        info=json.dumps(schema, indent=2),
    )

    # Create the message list
    messages = [HumanMessage(content=p)] + state.messages

    # Invoke the model with the messages
    response = await structured_model.ainvoke(messages)
    
    # Return the queries
    return {
        "queries": response.queries
    }


def continue_to_search(state: State):
    """Generate Send objects for each query."""
    if not state.queries:
        return []
    
    # Return a list of `Send` objects
    # Each `Send` object consists of the name of a node in the graph
    # as well as the state to send to that node
    return [Send("search_node", {"query": q}) for q in state.queries]


async def search_node(state: SearchState):
    """Search the web for the given query."""
    # Use a single client instance
    tavily = TavilyClient()
    
    # Access query properly, depending on if it's a SearchState or dict
    query = state.query if hasattr(state, 'query') else state.get("query")
    
    # Perform the search using asyncio.to_thread since tavily.search is a blocking call
    results = await asyncio.to_thread(
        lambda: tavily.search(query)
    )

    # Return the search results
    return {
        "search_results": [results]
    }


async def continue_to_extract(state: State):
    """Continue to the extract node."""
    return [Send("crawl_and_extract", {"search_result": s}) for s in state.search_results]


async def crawl_and_extract(state: ResultState):
    """Crawl and extract the information from the search results."""
    # Get the client
    tavily = TavilyClient()

    # Get the URL from the search result
    url = state["search_result"]["results"][0].get("url", None)

    if url is None:
        return {"suppliers": []}
    
    # Check if this is a supplier directory or business website
    website_type = check_for_business_website(url)
    # print(f"Processing URL: {url} (Type: {website_type})")
    
    # Extract content from URL using asyncio.to_thread for blocking API call
    extracted_info = await asyncio.to_thread(
        lambda: tavily.extract(url, extract_depth="advanced")
    )

    # Get the raw content from the extraction
    try:
        content = extracted_info.get("results")[0]["raw_content"]
    except (KeyError, IndexError, TypeError):
        print(f"Error: Could not extract content from {url}")
        return {"suppliers": []}

    # Initialize the model
    raw_model = init_model()
    structured_model = raw_model.with_structured_output(Supplier)
    
    # Extract structured supplier information
    response = await structured_model.ainvoke(content)
    
    # If email is missing, try to crawl for it
    if response.contact_details.email is None:
        try:
            # Use asyncio.to_thread for crawling (blocking operation)
            crawled_response = await asyncio.to_thread(
                lambda: tavily.crawl(url, instructions="Extract the email address of the supplier")
            )
            # Get new URL from crawled response
            crawled_url = crawled_response.get("results")[0]["url"]
            
            # Extract content from new URL
            crawled_extracted_info = await asyncio.to_thread(
                lambda: tavily.extract(crawled_url, extract_depth="advanced")
            )
            
            # Process content from crawled URL
            crawled_content = crawled_extracted_info.get("results")[0]["raw_content"]
            
            # Get updated structured information
            response = await structured_model.ainvoke(crawled_content)
        except Exception as e:
            print(f"Error during crawling for email: {str(e)}")

    # Return the extracted supplier information
    return {
        "suppliers": [response]
    }



# Create the graph
workflow = StateGraph(State, input=InputState, output=OutputState, config_schema=Configuration)

workflow.add_node(call_agent_model)
workflow.add_node(search_node)
workflow.add_node(crawl_and_extract)
workflow.add_edge("__start__", "call_agent_model")
workflow.add_conditional_edges("call_agent_model", continue_to_search)
workflow.add_conditional_edges("search_node", continue_to_extract)   
workflow.add_edge("crawl_and_extract", "__end__")

graph = workflow.compile()


if __name__ == "__main__":
    
    asyncio.run(graph.ainvoke({
        "company_name": "InnoMed Devices", 
        "company_info": """Industry: Medical Device Manufacturing

                                Size: 65 employees

                                Location: Pune, India

                                Annual Revenue: ₹18 crore""", 
        "procurement_requirement": "InnoMed needs to source medical-grade polymers and electronic components for their new line of portable diagnostic devices. They require suppliers who can provide materials that meet ISO 13485 and FDA compliance standards, with complete traceability documentation. The initial order will be for components to produce 10,000 units with potential for ongoing supply relationship."
    }))

graph.name = "search-graph"

    



