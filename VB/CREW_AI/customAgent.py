from VB.config import API_KEY
from crewai import Agent,Task,Crew,LLM

agent = Agent(
    role = "Motivational Speaker",
    goal = "Create an inspirational linked in post for job seekers",
    backstory = "An experienced carrier mentor who inspires others through writing",
    llm = LLM(model="gemini/gemini-3.5-flash",api_key=API_KEY)
)

task = Task(
    description = "Write a short linked post to motivate job seekers on topic = {topic}",
    expected_output = "Clean and humanised linkedin post",
    agent = agent
)

crew = Crew(
    agents = [agent],
    tasks = [task]
)

print(crew.kickoff(inputs={"topic":"Dealing with rejections"}))