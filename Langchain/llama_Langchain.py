from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2:latest")
response = model.invoke("what is the difference between Langchain and Langgraph, tell me in clear points wise")

print(response.content)