from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(name=data["name"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"]):
        token = create_access_token(identity=str(user.id))
        return jsonify(access_token=token)

    return jsonify({"msg": "Invalid credentials"}), 401


# simple health check endpoint to verify auth blueprint is loaded
@auth_bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "service": "auth"})


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    """Return basic information about the current user."""
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "reputation": user.reputation
    })
