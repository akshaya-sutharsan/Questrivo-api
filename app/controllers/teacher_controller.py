from flask import request
from app.extensions import db
from app.models.teacher_model import Teacher
from app.utils import success, error


def list_teachers():
    teachers = Teacher.query.all()
    return success([t.to_dict() for t in teachers])


def get_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return error("Teacher not found", 404)
    return success(teacher.to_dict())


def update_teacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return error("Teacher not found", 404)

    data = request.get_json() or {}
    teacher.school_name = data.get("school_name", teacher.school_name)
    teacher.subject_specialty = data.get("subject_specialty", teacher.subject_specialty)
    db.session.commit()
    return success(teacher.to_dict(), "Updated")
