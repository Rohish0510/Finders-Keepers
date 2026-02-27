from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.claim import Claim
from app.models.item import Item
from app.models.user import User

claim_bp = Blueprint("claims", __name__)

@claim_bp.route("/<int:item_id>", methods=["POST"])
@jwt_required()
def create_claim(item_id):
    user_id = get_jwt_identity()

    item = Item.query.get_or_404(item_id)

    if item.status != "open":
        return jsonify({"msg": "Item already claimed or closed"}), 400

    if item.user_id == user_id:
        return jsonify({"msg": "You cannot claim your own item"}), 400

    claim = Claim(
        item_id=item_id,
        claimant_id=user_id
    )

    db.session.add(claim)
    db.session.commit()

    return jsonify({"msg": "Claim submitted"}), 201

@claim_bp.route("/review/<int:claim_id>", methods=["PUT"])
@jwt_required()
def review_claim(claim_id):
    user_id = get_jwt_identity()
    data = request.json

    claim = Claim.query.get_or_404(claim_id)
    item = Item.query.get(claim.item_id)

    if item.user_id != user_id:
        return jsonify({"msg": "Only item owner can review claim"}), 403

    if data["action"] == "approve":
        claim.status = "approved"
        item.status = "claimed"

        claimant = User.query.get(claim.claimant_id)
        claimant.reputation += 10

    elif data["action"] == "reject":
        claim.status = "rejected"

    db.session.commit()

    return jsonify({"msg": f"Claim {data['action']}ed successfully"})