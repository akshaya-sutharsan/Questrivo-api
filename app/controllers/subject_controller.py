from flask import request
from app.extensions import db
from app.models.subject_model import Subject
from app.utils import success, error


def list_subjects():
    subjects = Subject.query.all()
    return success([s.to_dict() for s in subjects])


def create_subject():
    data = request.get_json() or {}
    if not data.get("name") or not data.get("grade"):
        return error("name and grade are required")

    subject = Subject(name=data["name"], grade=data["grade"])
    db.session.add(subject)
    db.session.commit()
    return success(subject.to_dict(), "Subject created", 201)


def delete_subject(subject_id):
    subject = Subject.query.get(subject_id)
    if not subject:
        return error("Subject not found", 404)
    db.session.delete(subject)
    db.session.commit()
    return success(message="Deleted")
