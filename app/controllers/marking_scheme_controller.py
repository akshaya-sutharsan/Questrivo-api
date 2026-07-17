from app.extensions import db
from app.models.exam_model import Exam
from app.models.marking_scheme_model import MarkingScheme
from app.services.marking_scheme_service import generate_marking_scheme
from app.utils import success, error


def create_marking_scheme(exam_id):
    exam = Exam.query.get(exam_id)
    if not exam:
        return error("Exam not found", 404)

    if MarkingScheme.query.filter_by(exam_id=exam_id).first():
        return error("Marking scheme already exists for this exam", 409)

    content = generate_marking_scheme(exam.content)
    scheme = MarkingScheme(exam_id=exam_id, content=content)
    db.session.add(scheme)
    db.session.commit()
    return success(scheme.to_dict(), "Marking scheme generated", 201)


def get_marking_scheme(exam_id):
    scheme = MarkingScheme.query.filter_by(exam_id=exam_id).first()
    if not scheme:
        return error("Marking scheme not found", 404)
    return success(scheme.to_dict())
