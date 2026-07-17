from flask import request
from flask_jwt_extended import create_access_token
from app.extensions import db
from app.models.user_model import User
from app.models.teacher_model import Teacher
from app.models.student_model import Student
from app.utils import success, error


def register():
    data = request.get_json() or {}
    required = ["name", "email", "password", "role"]
    if not all(data.get(f) for f in required):
        return error("name, email, password and role are required")

    if User.query.filter_by(email=data["email"]).first():
        return error("Email already registered", 409)

    user = User(name=data["name"], email=data["email"], role=data["role"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.flush()

    if data["role"] == "teacher":
        db.session.add(Teacher(user_id=user.id, school_name=data.get("school_name")))
    elif data["role"] == "student":
        db.session.add(Student(user_id=user.id, grade=data.get("grade")))

    db.session.commit()
    token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return success({"user": user.to_dict(), "token": token}, "Registered successfully", 201)


def login():
    data = request.get_json() or {}
    user = User.query.filter_by(email=data.get("email")).first()
    if not user or not user.check_password(data.get("password", "")):
        return error("Invalid credentials", 401)

    token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return success({"user": user.to_dict(), "token": token}, "Login successful")
