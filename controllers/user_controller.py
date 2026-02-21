from flask import request, jsonify
from models.user import User

class UserController:
    def __init__(self):
        self.user = User()

    def create_user(self, current_user):
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        result = self.user.create_user(data)
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
    
    def get_all_users(self, current_user):
        result = self.user.get_all_users()
        return jsonify(result), 200
    
    def get_user_by_id(self, current_user, user_id):
        result = self.user.get_user_by_id(user_id)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result), 200
    
    def update_user(self, current_user, user_id):
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        result = self.user.update_user(user_id, data)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result), 200
    
    def delete_user(self, current_user, user_id):
        result = self.user.delete_user(user_id)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result), 200