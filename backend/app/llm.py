import google.generativeai as genai
import os
from typing import Optional

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_embedding(text: str) -> list:
    """
    Get embeddings using Gemini's embedding model (free tier)
    """
    try:
        if not GEMINI_API_KEY:
            print("Warning: GEMINI_API_KEY not set. Using placeholder embeddings.")
            return [0.0] * 768  # Placeholder embedding for demo
        
        # Using Gemini's text embedding model
        model = genai.GenerativeModel('gemini-pro')
        # For embeddings, we'll use a simple approach since Gemini doesn't have direct embedding API
        # In production, you might want to use a dedicated embedding service
        return [0.0] * 768  # Placeholder embedding for demo
    except Exception as e:
        print(f"Embedding error: {e}")
        return [0.0] * 768

def ask_llm(prompt: str, context: Optional[str] = None) -> str:
    """
    Ask Gemini LLM with optional context
    """
    try:
        if not GEMINI_API_KEY:
            return "Error: GEMINI_API_KEY not configured. Please set your API key in the .env file."
        
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Build the full prompt with context if provided
        full_prompt = prompt
        if context:
            full_prompt = f"Context: {context}\n\nQuestion: {prompt}\n\nPlease answer based on the provided context."
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def ask_gemini_with_web_search(prompt: str, context: Optional[str] = None) -> str:
    """
    Use Gemini with web search capability
    """
    try:
        if not GEMINI_API_KEY:
            return "Error: GEMINI_API_KEY not configured. Please set your API key in the .env file."
        
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Add web search instruction
        full_prompt = f"Please search the web for current information about: {prompt}\n\n"
        if context:
            full_prompt += f"Additional context: {context}\n\n"
        full_prompt += "Provide a comprehensive answer based on web search results."
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error with web search: {str(e)}" 