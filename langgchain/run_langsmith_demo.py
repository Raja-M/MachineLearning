"""
Small demo runner that imports ChatOllama safely. This file avoids the previous name collision with the
installed `langsmith` package.

It only tests imports and will not call remote APIs unless you uncomment the llm.invoke call.
"""
import os
from getpass import getpass

# Try to import ChatOllama from langchain_ollama and print a short message.
try:
    from langchain_ollama.chat_models import ChatOllama
except Exception:
    import traceback
    print("Import failed, full traceback:")
    traceback.print_exc()
else:
    print("Import succeeded:", ChatOllama)

# Minimal safe usage example (commented out to avoid remote calls):
if False:
    api_key = os.environ.get("LANGCHAIN_API_KEY")
    if not api_key:
        api_key = getpass("Enter LANGCHAIN_API_KEY: ")
    os.environ["LANGCHAIN_API_KEY"] = api_key
    os.environ["LANGCHAIN_ENDPOINT"] = os.environ.get("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
    llm = ChatOllama(temperature=0.0, model="llama3.2:1b-instruct-fp16")
    print(llm.invoke("hello"))
