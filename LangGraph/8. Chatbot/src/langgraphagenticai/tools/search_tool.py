from langgraph.prebuilt import ToolNode

try:
    # Preferred package (new)
    from langchain_tavily import TavilySearch
except ImportError:
    # Backward-compatible fallback (older package)
    from langchain_community.tools.tavily_search import TavilySearchResults as TavilySearch

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools=[TavilySearch(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)
