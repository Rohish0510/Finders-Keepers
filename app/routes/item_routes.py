from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.item import Item
from app.models.user import User
from app.services.matching_service import find_similar

item_bp = Blueprint("items", __name__)

@item_bp.route("/", methods=["POST"])
@jwt_required()
def create_item():
    user_id = get_jwt_identity()
    data = request.json

    item = Item(
        title=data["title"],
        description=data["description"],
        category=data["category"],
        location=data["location"],
        type=data["type"],  # lost / found
        user_id=user_id
    )

    db.session.add(item)
    db.session.commit()

    # AI similarity matching
    existing_items = Item.query.filter(Item.id != item.id).all()
    corpus = [i.description for i in existing_items]

    if corpus:
        similarity_scores = find_similar(item.description, corpus)
        matches = [
            {"item_id": existing_items[i].id, "score": similarity_scores[i]}
            for i in range(len(similarity_scores))
            if similarity_scores[i] > 0.7
        ]
    else:
        matches = []

    return jsonify({
        "msg": "Item created",
        "matches": matches
    }), 201


@item_bp.route("/", methods=["GET"])
def get_all_items():
    items = Item.query.all()

    return jsonify([
        {
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "category": item.category,
            "location": item.location,
            "type": item.type,
            "status": item.status
        }
        for item in items
    ])