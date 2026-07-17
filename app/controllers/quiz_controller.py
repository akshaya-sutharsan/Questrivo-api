from flask import request
from app.extensions import db
from app.models.quiz_model import Quiz
from app.models.subject_model import Subject
from app.models.lesson_model import Lesson
from app.services.quiz_generator import generate_quiz
from app.utils import success, error


def create_quiz():
    data = request.get_json() or {}
    required = ["subject_id", "lesson_id", "difficulty"]
    if not all(data.get(f) for f in required):
        return error(f"Missing required fields: {required}")

    subject = Subject.query.get(data["subject_id"])
    lesson = Lesson.query.get(data["lesson_id"])
    if not subject or not lesson:
        return error("Subject or lesson not found", 404)

    content = generate_quiz(
        subject=subject.name,
        unit=lesson.unit_name,
        difficulty=data["difficulty"],
        count=data.get("count", 10),
    )

    quiz = Quiz(
        teacher_id=data.get("teacher_id"),
        subject_id=data["subject_id"],
        lesson_id=data["lesson_id"],
        content=content,
    )
    db.session.add(quiz)
    db.session.commit()
    return success(quiz.to_dict(), "Quiz generated", 201)


def list_quizzes():
    subject_id = request.args.get("subject_id")
    query = Quiz.query
    if subject_id:
        query = query.filter_by(subject_id=subject_id)
    return success([q.to_dict() for q in query.order_by(Quiz.created_at.desc()).all()])
