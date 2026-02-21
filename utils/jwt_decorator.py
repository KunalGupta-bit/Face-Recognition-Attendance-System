from functools import wraps
from flask import request, jsonify, current_app
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if token is provided in the header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Expecting "Bearer <token>"

        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            current_user_email = data['sub']  # Flask-JWT-Extended uses 'sub' for identity
        except Exception as e:
            return jsonify({"error": "Token is invalid!", "message": str(e)}), 401

        return f(*args, **kwargs)

    return decorated