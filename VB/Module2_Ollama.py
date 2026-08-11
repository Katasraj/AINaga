import requests
import json

result = requests.post(
  url="http://localhost:11434/api/generate",
  data=json.dumps({
    "model": "llama model",
    "prompt": "what is Langchain",
    "stream":False
  })
)

data = result.json()
print(data["response"])