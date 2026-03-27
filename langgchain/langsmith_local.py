import os
from getpass import getpass
from langchain_ollama.chat_models import ChatOllama

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
 
os.environ["LANGCHAIN_PROJECT"] = "aai-langchain-course-langsmith-starter-ollama"
 
model_name = "llama3.2:1b-instruct-fp16"

# initialize one LLM with temperature 0.0, this makes the LLM more deterministic
llm = ChatOllama(temperature=0.0, model=model_name)

llm.invoke("hello")
