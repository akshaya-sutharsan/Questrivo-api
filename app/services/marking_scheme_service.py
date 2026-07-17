from app.utils import read_prompt
from app.services.ai_service import generate_text


def generate_marking_scheme(exam_content):
    prompt = read_prompt("marking_prompt.txt", exam_content=exam_content)
    return generate_text(prompt)
