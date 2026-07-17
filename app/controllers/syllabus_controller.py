from flask import request
from app.extensions import db
from app.models.syllabus_model import Syllabus
from app.utils import success, error


def list_syllabus():
    subject_id = request.args.get("subject_id")
    query = Syllabus.query
    if subject_id:
        query = query.filter_by(subject_id=subject_id)
    return success([s.to_dict() for s in query.all()])


def create_syllabus():
    data = request.get_json() or {}
    if not data.get("subject_id") or not data.get("grade"):
        return error("subject_id and grade are required")

    syllabus = Syllabus(
        subject_id=data["subject_id"], grade=data["grade"], content=data.get("content")
    )
    db.session.add(syllabus)
    db.session.commit()
    return success(syllabus.to_dict(), "Syllabus created", 201)
