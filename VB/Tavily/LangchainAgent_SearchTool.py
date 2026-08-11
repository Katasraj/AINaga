from tavily import TavilyClient
from langchain_openai import ChatOpenAI

# Tavily
client = TavilyClient(api_key="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")

# Search
search_result = client.search(
    query="Who is the Deputy Chief Minister of Andhra Pradesh?"
)

# LLM
llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)

prompt = f"""
Answer the question using the information below.

Question:
Who is the Deputy Chief Minister of Andhra Pradesh?

Search results:
{search_result}
"""

response = llm.invoke(prompt)

print(response.content)