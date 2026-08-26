from langchain_core.prompts import PromptTemplate

################ Single-Turn Prompt Template ################
single_prompt = PromptTemplate.from_template(
    """ Explain {topic} in simple telugu"""
)

formatted_prompt = single_prompt.format(
    topic = "Generative AI"
)

print(formatted_prompt)

print(100*"*")

################ Dynamic Variables ################
dynamic_prompt = PromptTemplate.from_template(
    """ Create a {days}-day travel plan for {destination}.
    Budget: {budget}
    language: {language}
    """
)

dynamic_formatted_prompt = dynamic_prompt.format(
    destination="Goa",
    days=3,
    budget="Medium",
    language="English"
)

print(dynamic_formatted_prompt)

print(100*"*")

################ Chat Prompt Template ################

from langchain_core.prompts import ChatPromptTemplate
Chatprompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a friendly telugu teacher"
        ),
        (
            "human",
            "Explain {topic}"
        )
    ])
messages = Chatprompt.format_messages(
    topic="Prompt Engineering"
)
print(messages)

print(100*"*")

################ Multi Turn Chat or Conversation ################

from langchain_core.messages import HumanMessage

messages = [
    HumanMessage(
        content="Who is Mohammad Ali"
    ),
    HumanMessage(
        content="What is his original name"
    )

]


################ Chat Prompt Template + History ################

from langchain_core.prompts import (
    ChatPromptTemplate,MessagesPlaceholder
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant"
    ),
    MessagesPlaceholder(
        variable_name="history"
    ),
    (
        "human",
        "{question}"
    )
])

history = [
    HumanMessage(
        content="Who is Mohammad Ali?"
    )
]

messages = prompt.format_messages(
    history=history,
    question="What is his original name?"
)