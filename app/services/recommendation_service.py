from app.models.progress_model import Progress


def get_recommendations(student_id):
    records = (
        Progress.query.filter_by(student_id=student_id)
        .order_by(Progress.recorded_at.desc())
        .limit(10)
        .all()
    )
    if not records:
        return {"message": "No progress data yet.", "weak_subjects": []}

    scores_by_subject = {}
    for r in records:
        scores_by_subject.setdefault(r.subject_id, []).append(r.score)

    weak_subjects = [
        subject_id
        for subject_id, scores in scores_by_subject.items()
        if sum(scores) / len(scores) < 50
    ]

    return {
        "message": "Focus more on your weaker subjects.",
        "weak_subjects": weak_subjects,
    }
