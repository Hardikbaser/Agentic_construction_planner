def site_report_prompt(data):
    return f"""
Generate a professional construction site report.

Follow this structure strictly:

1. Project Details
2. Work Completed
3. Materials Used
4. Workforce Details
5. Site Conditions
6. Issues / Delays
7. Safety Observations
8. Conclusion

Use:
- Formal tone
- Civil engineering terminology
- Clear headings

Data:
{data}
"""