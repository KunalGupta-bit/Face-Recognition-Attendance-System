from flask import Flask
from pymongo import MongoClient
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    client = MongoClient(app.config['MONGO_URI'])
    app.db = client["attendance_db"]

    @app.route('/')
    def home():
        return {"message": "MongoDB Connected Successfully"}
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
