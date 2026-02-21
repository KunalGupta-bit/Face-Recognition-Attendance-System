import token

from flask import current_app
import jwt
from flask import current_app
from datetime import datetime, timedelta
import bcrypt


class Admin:

    def create_admin(self, data):
        db = current_app.db

        # Check if admin already exists
        if db.admins.find_one({"email": data["email"]}):
            return {"error": "Admin already exists"}

        # Hash password
        hashed_password = bcrypt.hashpw(
            data["password"].encode('utf-8'),
            bcrypt.gensalt()
        )

        admin_data = {
            "name": data["name"],
            "email": data["email"],
            "password": hashed_password
        }

        result = db.admins.insert_one(admin_data)

        return {
            "message": "Admin created successfully",
            "admin_id": str(result.inserted_id)
        }

    def login_admin(self, data):
        db = current_app.db

        admin = db.admins.find_one({"email": data["email"]})

        if not admin:
            return {"error": "Admin not found"}

        if bcrypt.checkpw(
            data["password"].encode('utf-8'),
            admin["password"]
        ):
            

            return {
                "token": jwt.encode(
                    {
                        "admin_id": str(admin["_id"]),
                        "exp": datetime.utcnow() + timedelta(hours=2)
                    },
                    current_app.config['SECRET_KEY'],
                    algorithm="HS256"
                )
            }
        else:
            return {"error": "Invalid password"}
    
    def get_all_admins(self):
        db = current_app.db
        admins = db.admins.find()
        return [{"admin_id": str(admin["_id"]), "name": admin["name"], "email": admin["email"]} for admin in admins]