"""Utility functions used in our graph."""

from typing import Literal, Optional

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig

from enrichment_agent.configuration import Configuration
from tavily import TavilyClient

from typing import List


def check_for_business_website(url: str) -> Literal["business_website", "supplier_directory"]:
    """Check if the given URL is a business website."""
    supplier_directories = ["indiamart", "tradeindia", "justdial", "yellowpages"]
    
    # Check if any of the supplier directory names are in the URL
    if any(directory in url.lower() for directory in supplier_directories):
        return "supplier_directory"
    else:
        return "business_website"


def get_message_text(msg: AnyMessage) -> str:
    """Get the text content of a message."""
    content = msg.content
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return content.get("text", "")
    else:
        txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
        return "".join(txts).strip()


def init_model(config: Optional[RunnableConfig] = None) -> BaseChatModel:
    """Initialize the configured chat model."""
    configuration = Configuration.from_runnable_config(config)
    fully_specified_name = configuration.model
    if "/" in fully_specified_name:
        provider, model = fully_specified_name.split("/", maxsplit=1)
    else:
        provider = None
        model = fully_specified_name
    return init_chat_model(model, model_provider=provider)

def get_supplier_directory_info(url: str) -> str:
    """Get the supplier directory info from the URL."""
    if "indiamart" in url:
        return "indiamart"
    elif "tradeindia" in url:
        return "tradeindia"
    elif "justdial" in url: 
        return "justdial"
    elif "yellowpages" in url:
        return "yellowpages"
    else:
        return None



