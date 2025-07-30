import requests
import os
from typing import Optional

# Free web search alternatives
def web_search_free(query: str) -> str:
    """
    Free web search using DuckDuckGo API (no API key required)
    """
    try:
        # Using DuckDuckGo Instant Answer API (free, no API key)
        url = "https://api.duckduckgo.com/"
        params = {
            "q": query,
            "format": "json",
            "no_html": "1",
            "skip_disambig": "1"
        }
        
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Extract relevant information
        if data.get("Abstract"):
            return data["Abstract"]
        elif data.get("Answer"):
            return data["Answer"]
        elif data.get("RelatedTopics") and len(data["RelatedTopics"]) > 0:
            return data["RelatedTopics"][0].get("Text", "No specific information found.")
        else:
            return "No web search results found."
            
    except Exception as e:
        return f"Web search error: {str(e)}"

def web_search_wikipedia(query: str) -> str:
    """
    Free Wikipedia search using MediaWiki API
    """
    try:
        # Search Wikipedia
        search_url = "https://en.wikipedia.org/w/api.php"
        search_params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srlimit": 1
        }
        
        response = requests.get(search_url, params=search_params, timeout=10)
        data = response.json()
        
        if data.get("query", {}).get("search"):
            page_id = data["query"]["search"][0]["pageid"]
            
            # Get page content
            content_params = {
                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro": "1",
                "explaintext": "1",
                "pageids": page_id
            }
            
            content_response = requests.get(search_url, params=content_params, timeout=10)
            content_data = content_response.json()
            
            if content_data.get("query", {}).get("pages", {}).get(str(page_id), {}).get("extract"):
                return content_data["query"]["pages"][str(page_id)]["extract"][:500] + "..."
        
        return "No Wikipedia information found."
        
    except Exception as e:
        return f"Wikipedia search error: {str(e)}"

def web_search(query: str) -> str:
    """
    Main web search function - tries free alternatives first
    """
    # Try DuckDuckGo first
    result = web_search_free(query)
    if result and not result.startswith("Web search error"):
        return result
    
    # Fallback to Wikipedia
    return web_search_wikipedia(query) 