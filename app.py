from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from config import Config
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp

def create_app():                           #This is called the Application Factory Pattern.Instead of creating the app directly, we wrap it inside a function.
    app = Flask(__name__)
    app.config.from_object(Config)

    client = MongoClient(app.config['MONGO_URI'])
    app.db = client["attendance_db"]

    jwt = JWTManager(app)

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/api')

    @app.route('/')
    def home():
        return {"message": "MongoDB Connected Successfully"}
    
    return app

app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
