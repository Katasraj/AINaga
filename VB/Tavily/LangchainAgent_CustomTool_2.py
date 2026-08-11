from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

@tool
def add_numbers(a:int, b:int) -> int:
    '''Add two numbers'''
    return a+b

@tool
def multiply_numbers(a:int,b:int) -> int:
    ''' Multiply two numbers'''
    return a*b

# LLM
llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)


# Give the tool to the LLM
llm_with_tools = llm.bind_tools([add_numbers,multiply_numbers])

response = llm_with_tools.invoke(
    "what is 25+5 and what is 20*5"
)

print("LLM response:")
print(response.tool_calls)

if response.tool_calls:

    for tool_call in response.tool_calls:

        print("\nTool requested")
        print(tool_call['name'])

        print("\nArguments")
        print(tool_call['args'])

        if tool_call['name'] == 'add_numbers':
            result = add_numbers.invoke(tool_call["args"])

        elif tool_call['name'] == 'multiply_numbers':
            result = multiply_numbers.invoke(tool_call["args"])

        print("\nTool Result")
        print(result)