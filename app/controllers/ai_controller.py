from flask import request
from app.extensions import db
from app.models.ai_chat_model import AIChat
from app.services.chatbot_service import ask_tutor
from app.utils import success, error


def chat():
    data = request.get_json() or {}
    required = ["student_id", "grade", "subject", "question"]
    if not all(data.get(f) for f in required):
        return error(f"Missing required fields: {required}")

    response = ask_tutor(data["grade"], data["subject"], data["question"])

    chat_record = AIChat(
        student_id=data["student_id"], message=data["question"], response=response
    )
    db.session.add(chat_record)
    db.session.commit()
    return success(chat_record.to_dict(), "Response generated", 201)


def chat_history(student_id):
    records = AIChat.query.filter_by(student_id=student_id).order_by(
        AIChat.created_at.desc()
    ).all()
    return success([r.to_dict() for r in records])
