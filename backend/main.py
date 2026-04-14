import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from agents.planner import planner_agent
from agents.scheduler import scheduler_agent
from agents.report_agent import ReportAgent 

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request Model
class RequestData(BaseModel):
    goal: str = None
    query: str = None

# ✅ Serve Frontend
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# 🔥 FIXED STATIC PATH (IMPORTANT CHANGE)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.post("/plan")
def generate_plan(data: RequestData):
    user_input = data.goal or data.query

    print(f"🚀 Plan request: {user_input}")
    try:
        plan = planner_agent(user_input)
        return {"plan": str(plan)}
    except Exception as e:
        print("❌ Plan Error:", e)
        return {"plan": f"Error: {str(e)}"}



@app.post("/schedule")
def generate_schedule_route(data: RequestData):
    user_input = data.goal or data.query

    print(f"📅 Schedule request: {user_input}")
    try:
        schedule = scheduler_agent(user_input)
        return {"schedule": str(schedule)}
    except Exception as e:
        print("❌ Schedule Error:", e)
        return {"schedule": f"Error: {str(e)}"}



@app.post("/generate-report")
def generate_report(data: RequestData):
    user_input = data.goal or data.query

    print(f"🧾 Report request: {user_input}")

    try:
        agent = ReportAgent()
        steps = agent.plan(user_input)

        context = {}

        for step in steps:
            result = agent.act(step, context)

            if isinstance(result, dict):
                context.update(result)

        return {"final_report": context.get("report")}

    except Exception as e:
        print("❌ Report Error:", e)
        return {"final_report": f"Error: {str(e)}"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        timeout_keep_alive=60
    )