from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import exam_controller as ctrl

exam_bp = Blueprint("exams", __name__)

exam_bp.route("", methods=["POST"])(jwt_required()(ctrl.create_exam))
exam_bp.route("", methods=["GET"])(jwt_required()(ctrl.list_exams))
exam_bp.route("/<int:exam_id>", methods=["GET"])(jwt_required()(ctrl.get_exam))
exam_bp.route("/<int:exam_id>", methods=["DELETE"])(jwt_required()(ctrl.delete_exam))
