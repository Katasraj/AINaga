from langgraph.graph import END, StateGraph, MessagesState
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# LLM
# --------------------------------------------------

model = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter url",
    model="poolside_model"
)


# --------------------------------------------------
# Writer
# --------------------------------------------------

writer_prompt = ChatPromptTemplate.from_template(
    "Write a LinkedIn post about this topic: {topic}"
)

writer_chain = writer_prompt | model


# --------------------------------------------------
# Reviewer
# --------------------------------------------------

reviewer_prompt = ChatPromptTemplate.from_template(
    "Review the following LinkedIn post and suggest improvements: {post}"
)

reviewer_chain = reviewer_prompt | model


# --------------------------------------------------
# Create graph
# --------------------------------------------------

graph = StateGraph(MessagesState)


# --------------------------------------------------
# Writer node
# --------------------------------------------------

def writer_node(state: MessagesState):

    topic = state["messages"][-1].content

    post = writer_chain.invoke({
        "topic": topic
    })

    return {
        "messages": [
            AIMessage(content=post.content)
        ]
    }


# --------------------------------------------------
# Reviewer node
# --------------------------------------------------

def reviewer_node(state: MessagesState):

    post = state["messages"][-1].content

    review = reviewer_chain.invoke({
        "post": post
    })

    return {
        "messages": [
            AIMessage(content=review.content)
        ]
    }


# --------------------------------------------------
# Add nodes
# --------------------------------------------------

graph.add_node("Writer", writer_node)
graph.add_node("Reviewer", reviewer_node)


# --------------------------------------------------
# Entry point
# --------------------------------------------------

graph.set_entry_point("Writer")


# --------------------------------------------------
# Conditional logic
# --------------------------------------------------

def condition_check(state: MessagesState):

    if len(state["messages"]) >= 5:
        return END
    else:
        return "Reviewer"


# --------------------------------------------------
# Conditional edge
# --------------------------------------------------

graph.add_conditional_edges(
    "Writer",
    condition_check
)


# --------------------------------------------------
# Reviewer → Writer
# --------------------------------------------------

graph.add_edge(
    "Reviewer",
    "Writer"
)


# --------------------------------------------------
# Compile
# --------------------------------------------------

app = graph.compile()


# --------------------------------------------------
# Run
# --------------------------------------------------

response = app.invoke(
    {
        "messages": [
            HumanMessage(
                content="Job market in India?"
            )
        ]
    }
)


# --------------------------------------------------
# Print messages
# --------------------------------------------------

for message in response["messages"]:
    print("\n--------------------")
    print(message.content)