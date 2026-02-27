from flask import Flask, jsonify
from flask_cors import CORS
from app.config import Config
from app.extensions import db, jwt
from app.routes.auth_routes import auth_bp
from app.routes.item_routes import item_bp
from app.routes.claim_routes import claim_bp
from app.models import user, item, claim


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(item_bp, url_prefix="/api/items")
    app.register_blueprint(claim_bp, url_prefix="/api/claims")

    @app.route("/health")
    def health_check():
        return jsonify({"status": "running"}), 200

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)