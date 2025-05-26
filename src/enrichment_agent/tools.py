"""Tools for data enrichment.

This module contains functions that are directly exposed to the LLM as tools.
These tools can be used for tasks such as web searching and scraping.
Users can edit and extend these tools as needed.
"""

import json
from typing import Any, Dict, Optional, cast

import aiohttp
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg
from langgraph.prebuilt import InjectedState
from typing_extensions import Annotated
from tavily import TavilyClient
import asyncio

from enrichment_agent.schema import schema
from enrichment_agent.configuration import Configuration
from enrichment_agent.state import State, Supplier
from enrichment_agent.utils import init_model, check_for_business_website


async def search(
    query: str, *, config: Annotated[RunnableConfig, InjectedToolArg]
) -> Optional[list[dict[str, Any]]]:
    """Query a search engine.

    This function queries the web to fetch comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events. Provide as much context in the query as needed to ensure high recall.
    """
    configuration = Configuration.from_runnable_config(config)
    wrapped = TavilySearchResults(max_results=configuration.max_search_results)
    result = await wrapped.ainvoke({"query": query})
    return cast(list[dict[str, Any]], result)


async def _extract_url_async(url: str, extract_depth: str = "advanced") -> Dict[str, Any]:
    """Asynchronous wrapper for TavilyClient.extract."""
    return await asyncio.to_thread(
        lambda: TavilyClient().extract(url, extract_depth=extract_depth)
    )


_INFO_PROMPT = """You are doing web research on behalf of a user. You are trying to find out this information:

<info>
{info}
</info>

You just scraped the following website: {url}

Based on the website content below, extract the suppliers information including:
1. Name: The supplier's company name
2. Description: Brief description of what the supplier does
3. Standards Compliance: Any industry standards or regulations they comply with
4. Certifications: Any certifications or quality marks they have
5. Contact Details: Including email, phone, website, and address if available

<Website content>
{content}
</Website content>

Format the contact details as a structured object with email, phone, website, and address fields."""

# async def scrape_contact_details(supplier: Supplier) -> ContactDetails:
#     """Scrape the contact details of a supplier."""

#     tavily_client = TavilyClient()
#     result = tavily

        
async def scrape_websites(
    urls: list[str],
    *,
    state: Annotated[State, InjectedState],
    config: Annotated[RunnableConfig, InjectedToolArg],
) -> Optional[list[Supplier]]:
    """Scrape and summarize content of all the given URLs.

    Returns:
        list[Supplier]: A list of supplier information extracted from the scraped content.
    """
    suppliers = []
    urls_to_crawl = []
    # Create a client session for aiohttp
    async with aiohttp.ClientSession() as session:

        for url in urls:
            
            if check_for_business_website(url) == "supplier_directory":
                urls_to_crawl.append(url)
            else:
                result = await _extract_url_async(url)
                
            # Extract content from the first result
            if result and "results" in result and len(result["results"]) > 0:
                content = result["results"][0]["raw_content"]

                p = _INFO_PROMPT.format(
                    info=json.dumps(schema, indent=2),
                    url=url,
                    content=content,
                )

                raw_model = init_model(config)
                supplier = await raw_model.with_structured_output(Supplier).ainvoke(p)

                suppliers.append(supplier)

    return suppliers

def scrape_website(
    urls: list[str],
    *,
    state: Annotated[State, InjectedState],
    config: Annotated[RunnableConfig, InjectedToolArg],
) -> Optional[list[Supplier]]:
    """Scrape and summarize content of all the given URLs.

    Returns:
        list[Supplier]: A list of supplier information extracted from the scraped content.
    """

    pass
