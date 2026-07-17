from flask import request
from app.extensions import db
from app.models.student_model import Student
from app.utils import success, error


def list_students():
    students = Student.query.all()
    return success([s.to_dict() for s in students])


def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return error("Student not found", 404)
    return success(student.to_dict())


def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return error("Student not found", 404)

    data = request.get_json() or {}
    student.grade = data.get("grade", student.grade)
    student.school_name = data.get("school_name", student.school_name)
    db.session.commit()
    return success(student.to_dict(), "Updated")
