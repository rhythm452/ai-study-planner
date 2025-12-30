import streamlit as st
from datetime import datetime
import os
from openai import OpenAI

client = OpenAI()  # api_key auto env se uthayega


st.set_page_config(page_title="AI Study Planner", page_icon="📘")

st.title("📘 AI Study Planner")
st.write("Plan your studies smartly with AI")

#  User Inputs
exam_date = st.date_input("📅 Select your exam date")
subjects = st.text_input("📚 Enter subjects (comma separated)")
hours_per_day = st.slider("⏰ Hours you can study per day", 1, 16, 5)
today = datetime.today().date()
days_left = (exam_date - today).days


def generate_plan():
    today = datetime.today().date()
    days_left = (exam_date - today).days

    prompt = f"""
    Create a {days_left}-day study plan.
    Subjects: {subjects}
    Daily study hours: {hours_per_day}
    Make it realistic and motivating.
    """

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt
    )

    return response.output_text

#  Button
if st.button("Generate Study Plan"):
    if subjects == "" or days_left <= 0:
        st.error("Please enter valid details.")
    else:
        with st.spinner("Creating your study plan..."):
            plan = generate_plan()
            st.success("Here is your study plan 👇")
            st.text(plan)




