from flask import Blueprint, jsonify
from middleware.auth import authenticate, authorize_roles

protected_bp = Blueprint("protected", __name__)

@protected_bp.route("/admin", methods=["GET"])
@authenticate
@authorize_roles("Admin")
def admin_route():
    return jsonify({"message": "Welcome, Admin!"}), 200

@protected_bp.route("/moderator", methods=["GET"])
@authenticate
@authorize_roles("Moderator")
def moderator_route():
    return jsonify({"message": "Welcome, Moderator!"}), 200

@protected_bp.route("/user", methods=["GET"])
@authenticate
@authorize_roles("User", "Moderator", "Admin")
def user_route():
    return jsonify({"message": "Welcome, User!"}), 200
