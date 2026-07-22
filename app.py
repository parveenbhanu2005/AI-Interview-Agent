from flask import Flask, render_template, request, session
from utils.ai import generate_questions
from utils.evaluator import evaluate_answer
import re

app = Flask(__name__)
app.secret_key = "interview_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():

    name = request.form["name"]
    email = request.form["email"]
    role = request.form["role"]

    # Generate AI Questions
    response = generate_questions(role)

    # Extract numbered questions
    questions = re.findall(r"\d+\.\s.*", response)

    # Fallback
    if len(questions) == 0:
        questions = [q.strip() for q in response.split("\n") if q.strip()]

    # Limit to exactly 5 questions
    questions = questions[:5]

    session["name"] = name
    session["email"] = email
    session["role"] = role
    session["questions"] = questions
    session["current"] = 0
    session["answers"] = []

    return render_template(
        "interview.html",
        question=questions[0],
        number=1,
        total=len(questions)
    )


@app.route("/next", methods=["POST"])
def next_question():

    answer = request.form.get("answer", "").strip()

    questions = session.get("questions", [])
    current = session.get("current", 0)
    answers = session.get("answers", [])

    if current >= len(questions):

        total_score = 0

        for item in answers:
            match = re.search(r"Score:\s*(\d+)/10", item["evaluation"])
            if match:
                total_score += int(match.group(1))

        percentage = round((total_score / (len(answers) * 10)) * 100, 2) if answers else 0

        if percentage >= 80:
            performance = "Excellent"
        elif percentage >= 60:
            performance = "Good"
        elif percentage >= 40:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        return render_template(
            "result.html",
            name=session["name"],
            role=session["role"],
            answers=answers,
            total_score=total_score,
            percentage=percentage,
            performance=performance
        )

    question = questions[current]

    evaluation = evaluate_answer(question, answer)

    answers.append({
        "question": question,
        "answer": answer,
        "evaluation": evaluation
    })

    session["answers"] = answers

    current += 1
    session["current"] = current

    if current >= len(questions):

        total_score = 0

        for item in answers:
            match = re.search(r"Score:\s*(\d+)/10", item["evaluation"])
            if match:
                total_score += int(match.group(1))

        percentage = round((total_score / (len(answers) * 10)) * 100, 2) if answers else 0

        if percentage >= 80:
            performance = "Excellent"
        elif percentage >= 60:
            performance = "Good"
        elif percentage >= 40:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        return render_template(
            "result.html",
            name=session["name"],
            role=session["role"],
            answers=answers,
            total_score=total_score,
            percentage=percentage,
            performance=performance
        )

    return render_template(
        "interview.html",
        question=questions[current],
        number=current + 1,
        total=len(questions)
    )


if __name__ == "__main__":
    app.run(debug=True)