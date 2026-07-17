from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import ai_controller as ctrl

ai_bp = Blueprint("ai", __name__)

ai_bp.route("/chat", methods=["POST"])(jwt_required()(ctrl.chat))
ai_bp.route("/chat/student/<int:student_id>", methods=["GET"])(jwt_required()(ctrl.chat_history))
