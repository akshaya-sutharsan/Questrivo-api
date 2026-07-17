from datetime import datetime
from app.extensions import db


class AIChat(db.Model):
    __tablename__ = "ai_chats"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "message": self.message,
            "response": self.response,
            "created_at": self.created_at.isoformat(),
        }
