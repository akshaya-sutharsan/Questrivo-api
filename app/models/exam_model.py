from datetime import datetime
from app.extensions import db


class Exam(db.Model):
    __tablename__ = "exams"

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    exam_type = db.Column(db.String(50))
    difficulty = db.Column(db.String(20))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "teacher_id": self.teacher_id,
            "subject_id": self.subject_id,
            "grade": self.grade,
            "exam_type": self.exam_type,
            "difficulty": self.difficulty,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
        }
