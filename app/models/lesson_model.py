from app.extensions import db


class Lesson(db.Model):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    unit_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "subject_id": self.subject_id,
            "unit_name": self.unit_name,
            "description": self.description,
        }
