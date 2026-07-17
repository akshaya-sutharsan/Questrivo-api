from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import subject_controller as ctrl

subject_bp = Blueprint("subjects", __name__)

subject_bp.route("", methods=["GET"])(ctrl.list_subjects)
subject_bp.route("", methods=["POST"])(jwt_required()(ctrl.create_subject))
subject_bp.route("/<int:subject_id>", methods=["DELETE"])(jwt_required()(ctrl.delete_subject))
