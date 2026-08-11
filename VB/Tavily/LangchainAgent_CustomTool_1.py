from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


"""
Normal Python function → no @tool
Function that you want an agent to use as a tool → use @tool
"""

# Function used as an LLM/Agent tool — @tool is useful

"""
When you use @tool, you are converting/wrapping a normal Python function into a LangChain Tool that an 
LLM/Agent can potentially call.
"""

@tool
def add_numbers(a:int, b:int) -> int:
    '''Add two numbers'''
    return a+b


# print(add_numbers.name)
# print(add_numbers.description)

# LLM
llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)

"""bind_tools() tells the LLM You have access to this tool.
Tool = a function that you make available to the LLM to use when needed.
"""

# Give the tool to the LLM
llm_with_tools = llm.bind_tools([add_numbers])

response = llm_with_tools.invoke(
    "what is 25+5"
)

print("LLM response:")
print(response)

"""response.tool_calls is the LLM's request to use a tool, not the tool's result"""
# Check whether LLM requested a tool
if response.tool_calls:

    tool_call = response.tool_calls[0]

    print("\nTool requested:")
    print(tool_call["name"])

    print("\nArguments:")
    print(tool_call["args"])

    # Execute the tool
    result = add_numbers.invoke(tool_call["args"])

    print("\nTool result:")
    print(result)




"""
Nemotron + OpenRouter + LangChain bind_tools() is successfully supporting tool calling
"""