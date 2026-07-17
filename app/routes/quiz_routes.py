from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import quiz_controller as ctrl

quiz_bp = Blueprint("quizzes", __name__)

quiz_bp.route("", methods=["POST"])(jwt_required()(ctrl.create_quiz))
quiz_bp.route("", methods=["GET"])(jwt_required()(ctrl.list_quizzes))
