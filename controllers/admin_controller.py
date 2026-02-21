from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_jwt_extended import create_access_token
from models.admin import Admin

class AdminController:
    
    def __init__(self):
        self.admin = Admin()

    def register(self):
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        result = self.admin.create_admin(data)
        if "error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
    
    def login(self):
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        access_token = create_access_token(identity=data['email'])
        
        result = self.admin.login_admin(data)
        if "error" in result:
            return jsonify(result), 400
        result["access_token"] = access_token
        return jsonify(result), 200
    
    def get_all_admins(self):
        result = self.admin.get_all_admins()
        return jsonify(result), 200
