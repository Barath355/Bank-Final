from flask import Flask
from flask_cors import CORS
from backend.extensions.db import db
from backend.extensions.bcrypt import bcrypt
from backend.routes.auth_routes import auth_bp
from backend.routes.account_routes import account_bp
from backend.routes.transaction_routes import transaction_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    app.config.from_object("backend.config.Config")

    CORS(app)

    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(account_bp, url_prefix="/account")
    app.register_blueprint(transaction_bp, url_prefix="/transaction")

    return app