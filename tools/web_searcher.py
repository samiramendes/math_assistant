from langchain.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper

@tool("wikipedia-searcher-tool")
async def wikipedia_search(query: str) -> str:
    """
    Use this tool for information on the web via Wikipedia API. Worth using for general topics. Use precise questions
    """
    # Call the API
    try:
        wikipedia = WikipediaAPIWrapper()
        response = wikipedia.run(query)
        return str(response)
    except Exception as e:
        return (f"Failed to calculate the expression. Make sure it's a valid math expression using numbers and operators only (Error: {str(e)})"
        )