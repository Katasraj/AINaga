from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-20b", temperature=0)
#model = ChatGroq(model = "llama-3.1-8b-instant", temperature=0)
response = model.invoke("What is the capital of Uganda")
print(response.content)

