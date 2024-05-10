from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

import os

class BaseLLMClass:
    def __init__(self) -> None:
        load_dotenv()

    def get_llm(self, max_tokens=5000, temperature=1):
        return AzureChatOpenAI(
            openai_api_version=os.getenv("OPENAI_API_VERSION"),
            openai_api_key=os.getenv('AZURE_OPENAI_API_KEY'),
            azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
            azure_deployment=os.getenv("AZURE_DEPLOYMENT"),
            max_tokens=max_tokens,
            temperature=temperature
        )