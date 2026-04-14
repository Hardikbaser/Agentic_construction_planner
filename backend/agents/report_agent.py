from llm.generator import generate_site_report

class ReportAgent:

    def plan(self, query):
        return ["collect_data", "validate_data", "generate_report"]

    def act(self, step, context):

        if step == "collect_data":
            return {
                "project": "Residential Building",
                "location": "Bhopal",
                "weather": "Sunny",
                "workers": 20,
                "work_done": "Foundation completed",
                "materials": "Cement, Steel"
            }

        elif step == "validate_data":
            # simple validation
            if "work_done" not in context:
                context["work_done"] = "Not specified"
            return context

        elif step == "generate_report":
            report = generate_site_report(context)
            return {"report": report}