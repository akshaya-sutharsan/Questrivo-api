from app.utils import read_prompt
from app.services.ai_service import generate_text


def generate_quiz(subject, unit, difficulty, count=10):
    prompt = read_prompt(
        "quiz_prompt.txt",
        subject=subject,
        unit=unit,
        difficulty=difficulty,
        count=count,
    )
    return generate_text(prompt)
