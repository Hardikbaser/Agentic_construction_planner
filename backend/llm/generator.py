from groq import Groq
import os
from .prompts import site_report_prompt

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_site_report(data):
    prompt = site_report_prompt(data)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ UPDATED MODEL
        messages=[
            {"role": "system", "content": "You are a professional construction engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content