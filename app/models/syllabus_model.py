from app.extensions import db


class Syllabus(db.Model):
    __tablename__ = "syllabus"

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "subject_id": self.subject_id,
            "grade": self.grade,
            "content": self.content,
        }
