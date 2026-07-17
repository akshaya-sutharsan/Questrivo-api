from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import student_controller as ctrl

student_bp = Blueprint("students", __name__)

student_bp.route("", methods=["GET"])(jwt_required()(ctrl.list_students))
student_bp.route("/<int:student_id>", methods=["GET"])(jwt_required()(ctrl.get_student))
student_bp.route("/<int:student_id>", methods=["PUT"])(jwt_required()(ctrl.update_student))
