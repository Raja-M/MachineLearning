import os
from getpass import getpass
from langchain_ollama.chat_models import ChatOllama

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
 
os.environ["LANGCHAIN_PROJECT"] = "aai-langchain-course-langsmith-starter-ollama"

llm = ChatOllama(model="llama3.2:3b")
response = llm.invoke("Hello! How are you?")
print(response)