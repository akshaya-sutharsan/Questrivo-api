from flask import request
from app.extensions import db
from app.models.progress_model import Progress
from app.services.recommendation_service import get_recommendations
from app.utils import success, error


def record_progress():
    data = request.get_json() or {}
    required = ["student_id", "subject_id", "score"]
    if not all(f in data for f in required):
        return error(f"Missing required fields: {required}")

    progress = Progress(
        student_id=data["student_id"],
        subject_id=data["subject_id"],
        score=data["score"],
    )
    db.session.add(progress)
    db.session.commit()
    return success(progress.to_dict(), "Progress recorded", 201)


def list_progress(student_id):
    records = Progress.query.filter_by(student_id=student_id).order_by(
        Progress.recorded_at.desc()
    ).all()
    return success([r.to_dict() for r in records])


def recommendations(student_id):
    return success(get_recommendations(student_id))
