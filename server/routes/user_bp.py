from flask import Blueprint

from controllers.UserController import select, insert, remove

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/login', methods=['POST'])(select)
user_bp.route('/register', methods=['POST'])(insert)
user_bp.route('/delete/<int:id>', methods=['DELETE'])(remove)