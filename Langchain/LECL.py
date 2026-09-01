""" LangChain Expression Language (LECL)"""
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.3)

parser = StrOutputParser()

summary_prompt = PromptTemplate.from_template("Summarize {topic} in 3 simple lines")

example_prompt = PromptTemplate.from_template("Give 3 real-world examples of {topic}")

quiz_prompt = PromptTemplate.from_template("Give 3 quiz questions about {topic}")

summary_chain = summary_prompt | llm | parser
example_chain = example_prompt | llm | parser
quiz_chain = quiz_prompt | llm | parser

parallel_chain = RunnableParallel({
    "summary":summary_chain,
    "examples":example_chain,
    "quiz":quiz_chain
})

result = parallel_chain.invoke({
    "topic":"Generative AI"
})
print(result["summary"])
print(result["examples"])
print(result["quiz"])