from flask import request
from app.extensions import db
from app.models.question_model import Question
from app.utils import success, error


def list_questions(exam_id):
    questions = Question.query.filter_by(exam_id=exam_id).all()
    return success([q.to_dict() for q in questions])


def add_question(exam_id):
    data = request.get_json() or {}
    if not data.get("question_text"):
        return error("question_text is required")

    question = Question(
        exam_id=exam_id,
        question_text=data["question_text"],
        question_type=data.get("question_type"),
        marks=data.get("marks", 0),
    )
    db.session.add(question)
    db.session.commit()
    return success(question.to_dict(), "Question added", 201)


def delete_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        return error("Question not found", 404)
    db.session.delete(question)
    db.session.commit()
    return success(message="Deleted")
