import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from agents.planner import planner_agent
from agents.scheduler import scheduler_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
  
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestData(BaseModel):
    goal: str


@app.get("/")
def home():
   
    return FileResponse("frontend/index.html")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.post("/plan")
def generate_plan(data: RequestData):
    print(f"🚀 Plan request: {data.goal}")
    try:
        
        plan = planner_agent(data.goal)
        return {"plan": str(plan)}
    except Exception as e:
        print("❌ Plan Error:", e)
        return {"plan": f"Error: {str(e)}"}


@app.post("/schedule")
def generate_schedule_route(data: RequestData): 
    print(f"📅 Schedule request: {data.goal}")
    try:
        schedule = scheduler_agent(data.goal)
        return {"schedule": str(schedule)}
    except Exception as e:
        print("❌ Schedule Error:", e)
        return {"schedule": f"Error: {str(e)}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        
        timeout_keep_alive=60 
    )