from flask import Blueprint, request
from controllers.user_controller import create_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return create_user(request)
