from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import syllabus_controller as ctrl

syllabus_bp = Blueprint("syllabus", __name__)

syllabus_bp.route("", methods=["GET"])(ctrl.list_syllabus)
syllabus_bp.route("", methods=["POST"])(jwt_required()(ctrl.create_syllabus))
