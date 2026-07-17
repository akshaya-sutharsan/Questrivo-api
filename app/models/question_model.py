from app.extensions import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey("exams.id"), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50))
    marks = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "exam_id": self.exam_id,
            "question_text": self.question_text,
            "question_type": self.question_type,
            "marks": self.marks,
        }
