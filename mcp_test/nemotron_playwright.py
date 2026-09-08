import asyncio
import json
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()


MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


llm = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


async def main():

    server_params = StdioServerParameters(
        command="playwright-mcp",
        args=[]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            # Get Playwright MCP tools
            mcp_tools = await session.list_tools()

            tools = []

            for tool in mcp_tools.tools:

                tools.append({
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description or "",
                        "parameters": tool.inputSchema
                    }
                })

            print("MCP tools loaded:", len(tools))

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a browser automation agent. "
                        "Use the available Playwright tools to complete "
                        "the user's browser automation request."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        "Open https://rahulshettyacademy.com/loginpagePractise/, "
                        "enter username rahulshettyacademy in the username field, "
                        "enter password Learning@830$3mK2 in the password field, "
                        "select the Teacher option from the dropdown, "
                        "check the check box at I Agree to the terms and conditions,"
                        "and click Sign In."
                    )
                }
            ]

            while True:

                response = await llm.chat.completions.create(
                    model=MODEL,
                    messages=messages,
                    tools=tools,
                    tool_choice="auto"
                )

                assistant_message = response.choices[0].message

                # Add model response to conversation
                messages.append(assistant_message.model_dump(exclude_none=True))

                # No tool call means model has finished
                if not assistant_message.tool_calls:

                    print("\nNemotron:")
                    print(assistant_message.content)
                    break

                # Execute each requested tool
                for tool_call in assistant_message.tool_calls:

                    tool_name = tool_call.function.name

                    arguments = json.loads(
                        tool_call.function.arguments
                    )

                    print(f"\nNemotron called: {tool_name}")
                    print("Arguments:", arguments)

                    result = await session.call_tool(
                        tool_name,
                        arguments
                    )

                    # Convert MCP result to text
                    result_text = "\n".join(
                        getattr(content, "text", str(content))
                        for content in result.content
                    )

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result_text
                    })


if __name__ == "__main__":
    asyncio.run(main())