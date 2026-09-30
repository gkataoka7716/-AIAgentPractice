import os

from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2",
    base_url=os.getenv("OLLAMA_BASE_URL", "http://ollama:11434"),
)