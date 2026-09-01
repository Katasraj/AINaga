from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.3)

parser = StrOutputParser()

summary_prompt = PromptTemplate.from_template("Write a 10 words summary about {topic}")

summary_chain = summary_prompt | llm | parser

chain = {
    "topic":RunnablePassthrough(),
    "summary":summary_chain
}

result = chain.invoke("LangChain")

print("Original Topic: ",result["topic"])
print("Generated Summary: ",result["summary"])