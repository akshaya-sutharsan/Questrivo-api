from app.utils import read_prompt
from app.services.ai_service import generate_text


def ask_tutor(grade, subject, question):
    prompt = read_prompt("tutor_prompt.txt", grade=grade, subject=subject, question=question)
    return generate_text(prompt)
