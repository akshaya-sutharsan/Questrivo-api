from app.utils import read_prompt
from app.services.ai_service import generate_text


def generate_exam(subject, grade, unit, exam_type, difficulty):
    prompt = read_prompt(
        "exam_prompt.txt",
        subject=subject,
        grade=grade,
        unit=unit,
        exam_type=exam_type,
        difficulty=difficulty,
    )
    return generate_text(prompt)
