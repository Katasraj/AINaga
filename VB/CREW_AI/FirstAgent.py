from VB.config import API_KEY, MODEL
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent,Task,Crew,LLM

# model = ChatGoogleGenerativeAI(model=MODEL, api_key=API_KEY)
# response = model.invoke("What is your cut off date")
# print(response.content)

agent = Agent(
    role = "Motivational Speaker",
    goal = "Create an inspirational linked in post for job seekers",
    backstory = "An experienced carrier mentor who inspires others through writing",
    llm = LLM(model="gemini/gemini-3.5-flash",api_key=API_KEY)
)

task = Task(
    description = "Write a short linked post to motivate job seekers",
    expected_output = "Clean and crispy linkedin post",
    agent = agent
)

crew = Crew(
    agents = [agent],
    tasks = [task]
)

print(crew.kickoff())