from flask import Blueprint
from controllers.admin_controller import AdminController
from flask_jwt_extended import jwt_required, get_jwt_identity

admin_bp = Blueprint('admin', __name__)
admin_controller = AdminController()

@admin_bp.route('/register', methods=['POST'])
def register():
    return admin_controller.register()

@admin_bp.route('/login', methods=['POST'])
def login():
    return admin_controller.login()

@admin_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    # return {"email": current_user}, 200
    return {"message": "This is a protected route", "user": current_user}, 200

@admin_bp.route('/admins', methods=['GET'])
@jwt_required()
def get_all_admins():
    return admin_controller.get_all_admins()