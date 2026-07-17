from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import lesson_controller as ctrl

lesson_bp = Blueprint("lessons", __name__)

lesson_bp.route("", methods=["GET"])(ctrl.list_lessons)
lesson_bp.route("", methods=["POST"])(jwt_required()(ctrl.create_lesson))
