from flask import Blueprint
from controllers.user_controller import UserController
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)
user_controller = UserController()

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    current_user = get_jwt_identity()
    return user_controller.create_user(current_user)

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    current_user = get_jwt_identity()
    return user_controller.get_all_users(current_user)

@user_bp.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    current_user = get_jwt_identity()
    return user_controller.get_user_by_id(current_user, user_id)

@user_bp.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()
    return user_controller.update_user(current_user, user_id)

@user_bp.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return user_controller.delete_user(user_id)