from flask import current_app
from bson import ObjectId
from datetime import datetime

class User:
    def create_user(self, data):
        db = current_app.db

        if db.users.find_one({"email": data["email"]}):
            return {"error": "User already exists"}
        
        user_data = {
            "name": data["name"],
            "email": data["email"],
            "course": data.get("course"),
            "department": data.get("department"),
            "role": data.get("role", "student"),
            "image_path": data.get("image_path"),
            "face_embedding": [],
            "is_active": True,
            "created_at": datetime.utcnow()
        }

        result = db.users.insert_one(user_data)
        return {"message": "User created successfully", "user_id": str(result.inserted_id)}
    
    def get_all_users(self):
        db = current_app.db
        users = db.users.find()
        return [{"user_id": str(user["_id"]), "name": user["name"], "email": user["email"],  "course": user.get("course"), "department": user.get("department"), "role": user.get("role"), "image_path": user.get("image_path"), "is_active": user.get("is_active", True)} for user in users]
    
    def get_user_by_id(self, user_id):
        db = current_app.db
        user = db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return {"error": "User not found"}
        return {"user_id": str(user["_id"]), "name": user["name"], "email": user["email"],  "course": user.get("course"), "department": user.get("department"), "role": user.get("role"), "image_path": user.get("image_path"), "is_active": user.get("is_active", True)}
    
    def update_user(self, user_id, data):
        db = current_app.db
        result = db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})
        if result.matched_count == 0:
            return {"error": "User not found"}
        return {"message": "User updated successfully"}
    
    def delete_user(self, user_id):
        db = current_app.db
        result = db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            return {"error": "User not found"}
        return {"message": "User deleted successfully"}