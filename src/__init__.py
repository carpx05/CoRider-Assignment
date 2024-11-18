from flask import Flask
from src.extensions import mongo, bcrypt, cors
from src.routes.user_route import users_bp
from src.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(users_bp, url_prefix='/users')

    return app