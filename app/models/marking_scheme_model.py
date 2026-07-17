from app.extensions import db


class MarkingScheme(db.Model):
    __tablename__ = "marking_schemes"

    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey("exams.id"), nullable=False, unique=True)
    content = db.Column(db.Text)

    def to_dict(self):
        return {"id": self.id, "exam_id": self.exam_id, "content": self.content}
