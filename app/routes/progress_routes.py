from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import progress_controller as ctrl

progress_bp = Blueprint("progress", __name__)

progress_bp.route("", methods=["POST"])(jwt_required()(ctrl.record_progress))
progress_bp.route("/student/<int:student_id>", methods=["GET"])(jwt_required()(ctrl.list_progress))
progress_bp.route("/student/<int:student_id>/recommendations", methods=["GET"])(
    jwt_required()(ctrl.recommendations)
)
