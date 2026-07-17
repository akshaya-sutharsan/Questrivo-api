from flask import Blueprint
from app.controllers import auth_controller as ctrl

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/register", methods=["POST"])(ctrl.register)
auth_bp.route("/login", methods=["POST"])(ctrl.login)
