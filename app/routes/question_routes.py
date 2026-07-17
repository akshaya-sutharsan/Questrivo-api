from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers import question_controller as ctrl

question_bp = Blueprint("questions", __name__)

question_bp.route("/exam/<int:exam_id>", methods=["GET"])(jwt_required()(ctrl.list_questions))
question_bp.route("/exam/<int:exam_id>", methods=["POST"])(jwt_required()(ctrl.add_question))
question_bp.route("/<int:question_id>", methods=["DELETE"])(jwt_required()(ctrl.delete_question))
