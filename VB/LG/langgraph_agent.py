from langgraph.graph import END, StateGraph, MessagesState
from langchain_core.messages import HumanMessage, AIMessage
from langchain_tavily import TavilySearch
from langchain_openai import ChatOpenAI


# --------------------------------------------------
# LLM
# --------------------------------------------------

model = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)

# --------------------------------------------------
# Tavily
# --------------------------------------------------

search = TavilySearch(
    tavily_api_key = "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",
    max_results=3
)


# --------------------------------------------------
# Planner Node
# --------------------------------------------------

def planner_node(state: MessagesState):

    user_input = state["messages"][-1].content

    prompt = """
You are a smart planner.

The user will ask a question.

Your job is to create an exact search query
that can be used to search the internet.

Output ONLY the search query.
"""

    response = model.invoke(
        [
            HumanMessage(content=prompt),
            HumanMessage(content=user_input)
        ]
    )

    return {
        "messages": [
            AIMessage(content=response.content)
        ]
    }


# --------------------------------------------------
# Search Node
# --------------------------------------------------

def search_node(state: MessagesState):

    query = state["messages"][-1].content

    search_results = search.invoke(query)

    return {
        "messages": [
            AIMessage(content=str(search_results))
        ]
    }


# --------------------------------------------------
# Responder Node
# --------------------------------------------------

def responder_node(state: MessagesState):

    user_question = state["messages"][0].content

    search_results = state["messages"][-1].content

    prompt = """
You are a helpful responder.

Use the search results to answer the user's question.
"""

    response = model.invoke(
        [
            HumanMessage(content=prompt),
            HumanMessage(
                content=f"""
User Question:
{user_question}

Search Results:
{search_results}
"""
            )
        ]
    )

    return {
        "messages": [
            AIMessage(content=response.content)
        ]
    }


# --------------------------------------------------
# Create Graph
# --------------------------------------------------

graph = StateGraph(MessagesState)

graph.add_node("Planner", planner_node)
graph.add_node("Search", search_node)
graph.add_node("Responder", responder_node)

graph.set_entry_point("Planner")

graph.add_edge("Planner", "Search")
graph.add_edge("Search", "Responder")
graph.add_edge("Responder", END)


# --------------------------------------------------
# Compile
# --------------------------------------------------

agent = graph.compile()


# --------------------------------------------------
# Run
# --------------------------------------------------

agent_response = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Which stock perfomed well in BSE on 07/08/2026"
            )
        ]
    }
)

print("Agent Response:", agent_response["messages"][-1].content)

print("***********************************************************************************************************")

print(agent.get_graph().print_ascii())