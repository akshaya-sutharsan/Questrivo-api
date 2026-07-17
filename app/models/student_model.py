from app.extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    grade = db.Column(db.String(20))
    school_name = db.Column(db.String(150))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "grade": self.grade,
            "school_name": self.school_name,
        }
