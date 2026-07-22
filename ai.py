from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    timeout=60
)

def generate_questions(role):

    prompt = f"""
You are an expert technical interviewer.

Generate exactly 5 interview questions for a {role}.

Return ONLY the 5 questions as a numbered list.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content