from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words"
)

'''
This is called the Tavily Expression Language (LCEL)
output of one component becomes the input to the next)
'''
chain = prompt | llm

response = chain.invoke({"topic":"Tavily"})

print(response.content)