from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import marking_scheme_controller as ctrl

marking_scheme_bp = Blueprint("marking_schemes", __name__)

marking_scheme_bp.route("/exam/<int:exam_id>", methods=["POST"])(
    jwt_required()(ctrl.create_marking_scheme)
)
marking_scheme_bp.route("/exam/<int:exam_id>", methods=["GET"])(
    jwt_required()(ctrl.get_marking_scheme)
)
