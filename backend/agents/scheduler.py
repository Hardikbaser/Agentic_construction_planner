from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def scheduler_agent(goal):
    scheduler = Agent(
        role="Construction Scheduler",
        goal="Create timeline for construction tasks",
        backstory="Project manager",
        llm=llm,
        verbose=False
    )

    task = Task(
        description=f"""
        Goal: {goal}
        Create a 7-day schedule with tasks per day.
        """,
        expected_output="Daily schedule",
        agent=scheduler
    )

    crew = Crew(agents=[scheduler], tasks=[task])

    return crew.kickoff()