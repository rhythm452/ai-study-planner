from datetime import datetime
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Agent role (system prompt)
SYSTEM_PROMPT = """
You are an AI study planner for BTech students.
You ask questions step-by-step.
You create a realistic and motivating daily study plan.
Explain things clearly and simply.
"""

def ask_ai(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content


print(" Welcome to AI Study Planner")

#  Collect user input
exam_date = input("Enter your exam date (YYYY-MM-DD): ")
subjects = input("Enter subjects (comma separated): ")
hours_per_day = input("How many hours can you study per day? ")

#  Calculate days left
today = datetime.today()
exam_date = datetime.strptime(exam_date, "%Y-%m-%d")
days_left = (exam_date - today).days

#  Prompt for AI
user_prompt = f"""
Create a {days_left}-day study plan.

Subjects: {subjects}
Daily study hours: {hours_per_day}

Make it beginner-friendly and practical.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_prompt}
]

#  Get plan from AI
study_plan = ask_ai(messages)

print("\n📘 YOUR STUDY PLAN:\n")
print(study_plan)