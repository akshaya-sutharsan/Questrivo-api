from app.extensions import db


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    school_name = db.Column(db.String(150))
    subject_specialty = db.Column(db.String(150))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "school_name": self.school_name,
            "subject_specialty": self.subject_specialty,
        }
