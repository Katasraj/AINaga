from VB.config import API_KEY,FIRE_CRAWL,OPEN_ROUTER_KEY,POOLSIDE_MODEL
from crewai import Agent,Task,Crew,LLM

from crewai_tools import (
    FirecrawlSearchTool
)


search_tool = FirecrawlSearchTool(api_key=FIRE_CRAWL)

# Agent 1: Researcher
researcher = Agent(
    role="Current Affairs Researcher",
    goal = "Fetch top 5 current global news topics",
    backstory = "An expert news researcher with access to latest information",
    tools=[search_tool],
    llm = LLM(model=f"openrouter/{POOLSIDE_MODEL}",api_key=OPEN_ROUTER_KEY)
    #llm = LLM(model="gemini/gemini-3.5-flash",api_key=API_KEY)
)

# Agent 2: Summarizer
summarizer = Agent(
    role="Note Maker",
    goal = "Convert research into clear, short bullet points",
    backstory = "An expert in simplifying complex topics for fast reading",
    llm = LLM(model=f"openrouter/{POOLSIDE_MODEL}",api_key=OPEN_ROUTER_KEY)
    #llm = LLM(model="gemini/gemini-3.5-flash",api_key=API_KEY), to use gemini flash model
)

task1 = Task(
    description = "Search for the top 5 global news stories using the web",
    expected_output = "Top 5 global news stories and its details",
    agent = researcher
)

task2 = Task(
    description = "Take the news articles from previous task and write clear one line summaries for each",
    expected_output = "Summarized and consumable notes",
    agent = summarizer
)

current_affairs_crew = Crew(
    agents = [researcher,summarizer],
    tasks = [task1,task2]
)

print(current_affairs_crew.kickoff())

"""
model="openrouter/poolside/laguna-s-2.1:free"

you're effectively telling LiteLLM:

Provider = OpenRouter
Model    = poolside/laguna-s-2.1:free

LLM(
    model="provider/model-name"
)
          ↑
          └── tells LiteLLM where/how to route the request
          
          
LLM
The LLM is responsible for:

understanding the task
deciding what information it needs
interpreting results
producing an answer
Firecrawl

Firecrawl is responsible for:
searching/accessing web information

So:
LLM = Brain 🧠
Firecrawl = Web tool 🔎
"""
