from langgraph.graph import StateGraph, END, add_messages
from langchain_core.messages import HumanMessage
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver


# --------------------------------------------------
# LLM
# --------------------------------------------------
model = ChatOpenAI(
    api_key="api_key",
    base_url="base_url",
    model="poolside llm model"
)


class MyState(TypedDict):
    messages: Annotated[list, add_messages]
    #messages:list

graph = StateGraph(MyState)

memory = MemorySaver()

def chat_node(state:MyState):
    print("Inside chat_node, current_state = ", state)
    response = model.invoke(state["messages"])
    # state["messages"] = state["messages"] + [response]
    # return state
    return {"messages":[response]}

graph.add_node("Chat", chat_node)
graph.set_entry_point("Chat")

graph.add_edge("Chat",END)

agent = graph.compile(checkpointer=memory)

configuration1 = {
    "configurable":{
        "thread_id":1
    }
}

ans1 = agent.invoke({"messages": [HumanMessage(content = "My Name is Naga")]}, config=configuration1)
print(ans1)


ans2= agent.invoke({"messages": [HumanMessage(content = "What is my name")]}, config=configuration1)
print(ans2)

print("**************************************************************************************************************")

configuration2 = {
    "configurable":{
        "thread_id":2
    }
}

ans1 = agent.invoke({"messages": [HumanMessage(content = "My Name is ABC")]}, config=configuration2)
print(ans1)


ans2= agent.invoke({"messages": [HumanMessage(content = "What is my name")]}, config=configuration2)
print(ans2)