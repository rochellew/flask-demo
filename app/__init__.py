from flask import Flask
from .extensions import db, login_manager
from .models import User
from .blueprints.auth import auth_bp

def create_app():
    from dotenv import load_dotenv
    load_dotenv()

    app = Flask(__name__)
    app.jinja_env.autoescape = True
    app.config.from_prefixed_env() # reads FLASK_* .env variables
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///users.db")
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login" # type: ignore
    login_manager.login_message_category = "error"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    # app.register_blueprint(cryptids_bp)

    with app.app_context():
        db.create_all()

    return app