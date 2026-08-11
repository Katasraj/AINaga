from openai import OpenAI

client = OpenAI(
  base_url="http://localhost:11434/v1",
  #base_url="https://openrouter.ai/api/v1",
  api_key="key not require",
)

completion = client.chat.completions.create(
  # extra_headers={
  #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
  #   "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  # },
  model="llama model",
  messages=[
    {
      "role": "user",
      "content": "Is ollama called LLM?"
    }
  ]
)

print(completion.choices[0].message.content)