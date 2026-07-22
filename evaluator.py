from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    timeout=60
)

def evaluate_answer(question, answer):

    prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return in exactly this format:

Score: X/10

Strengths:
- ...

Weaknesses:
- ...

Correct Answer:
...
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Groq Error:", e)

        return f"""
Score: 0/10

Strengths:
- Unable to evaluate.

Weaknesses:
- AI server connection failed.

Correct Answer:
Evaluation could not be generated because of a network/API timeout.
"""