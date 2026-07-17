from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import teacher_controller as ctrl

teacher_bp = Blueprint("teachers", __name__)

teacher_bp.route("", methods=["GET"])(jwt_required()(ctrl.list_teachers))
teacher_bp.route("/<int:teacher_id>", methods=["GET"])(jwt_required()(ctrl.get_teacher))
teacher_bp.route("/<int:teacher_id>", methods=["PUT"])(jwt_required()(ctrl.update_teacher))
