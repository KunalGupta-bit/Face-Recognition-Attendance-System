from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from config import Config
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from routes.register_routes import register_bp
from routes.attendance_routes import attendance_bp


def create_app():
    """Create and configure the Flask application (application factory)."""
    app = Flask(__name__)
    app.config.from_object(Config)

    client = MongoClient(app.config['MONGO_URI'])
    app.db = client["attendance_db"]

    JWTManager(app)

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(register_bp, url_prefix='/api')
    app.register_blueprint(attendance_bp, url_prefix='/api')

    @app.route('/')
    def home():
        return {"message": "MongoDB Connected Successfully"}

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
