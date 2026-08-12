from langgraph.graph import StateGraph,END
from typing import TypedDict


class MyState(TypedDict):
    count : int

graph = StateGraph(MyState)

def increment_node(state:MyState):
    print("Inside increament_node, current state = ",state)
    state["count"] = state["count"] + 1
    print("Inside increament_node, modified state = ", state)
    print("===============================================")
    return state

graph.add_node("Increment", increment_node)
graph.set_entry_point("Increment")

def isCountReachedLimit(state:MyState):
    if state["count"] >= 5:
        return END
    else:
        return "Increment"

graph.add_conditional_edges("Increment",isCountReachedLimit)

agent = graph.compile()

response = agent.invoke({"count":0})

print(response)

