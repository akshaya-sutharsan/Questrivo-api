from flask import request
from app.extensions import db
from app.models.lesson_model import Lesson
from app.utils import success, error


def list_lessons():
    subject_id = request.args.get("subject_id")
    query = Lesson.query
    if subject_id:
        query = query.filter_by(subject_id=subject_id)
    return success([l.to_dict() for l in query.all()])


def create_lesson():
    data = request.get_json() or {}
    if not data.get("subject_id") or not data.get("unit_name"):
        return error("subject_id and unit_name are required")

    lesson = Lesson(
        subject_id=data["subject_id"],
        unit_name=data["unit_name"],
        description=data.get("description"),
    )
    db.session.add(lesson)
    db.session.commit()
    return success(lesson.to_dict(), "Lesson created", 201)
