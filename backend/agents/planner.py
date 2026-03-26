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

def planner_agent(goal):
    planner = Agent(
        role="Construction Planner",
        goal="Break goal into actionable construction steps",
        backstory="Expert civil engineer",
        llm=llm,
        verbose=False
    )

    task = Task(
        description=f"""
        Goal: {goal}
        Break into 6-8 actionable steps.
        """,
        expected_output="Step-by-step plan",
        agent=planner
    )

    crew = Crew(agents=[planner], tasks=[task])

    return crew.kickoff()