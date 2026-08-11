from tavily import TavilyClient

client = TavilyClient(api_key="api key")

response = client.search(
    query="Who is the Deputy Chief Minister of Andhra Pradesh?"
)

print(response)