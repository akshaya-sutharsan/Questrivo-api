from flask import request
from flask_jwt_extended import get_jwt_identity
from app.extensions import db
from app.models.exam_model import Exam
from app.models.subject_model import Subject
from app.services.exam_generator import generate_exam
from app.utils import success, error


def create_exam():
    data = request.get_json() or {}
    required = ["teacher_id", "subject_id", "grade", "unit", "exam_type", "difficulty"]
    if not all(data.get(f) for f in required):
        return error(f"Missing required fields: {required}")

    subject = Subject.query.get(data["subject_id"])
    if not subject:
        return error("Subject not found", 404)

    content = generate_exam(
        subject=subject.name,
        grade=data["grade"],
        unit=data["unit"],
        exam_type=data["exam_type"],
        difficulty=data["difficulty"],
    )

    exam = Exam(
        teacher_id=data["teacher_id"],
        subject_id=data["subject_id"],
        grade=data["grade"],
        exam_type=data["exam_type"],
        difficulty=data["difficulty"],
        content=content,
    )
    db.session.add(exam)
    db.session.commit()
    return success(exam.to_dict(), "Exam generated", 201)


def list_exams():
    teacher_id = request.args.get("teacher_id")
    query = Exam.query
    if teacher_id:
        query = query.filter_by(teacher_id=teacher_id)
    return success([e.to_dict() for e in query.order_by(Exam.created_at.desc()).all()])


def get_exam(exam_id):
    exam = Exam.query.get(exam_id)
    if not exam:
        return error("Exam not found", 404)
    return success(exam.to_dict())


def delete_exam(exam_id):
    exam = Exam.query.get(exam_id)
    if not exam:
        return error("Exam not found", 404)
    db.session.delete(exam)
    db.session.commit()
    return success(message="Deleted")
