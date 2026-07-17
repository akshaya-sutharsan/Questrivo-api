from datetime import datetime
from app.extensions import db


class Quiz(db.Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "teacher_id": self.teacher_id,
            "subject_id": self.subject_id,
            "lesson_id": self.lesson_id,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
        }
