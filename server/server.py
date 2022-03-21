from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from config import SECRET_KEY
from controllers.UserController import select, insert, remove
from models.User import db
from routes.user_bp import user_bp
import jwt

server = Flask(__name__)
CORS(server)
server.config.from_object('config')

db.init_app(server)
migrate = Migrate(server, db)

server.register_blueprint(user_bp, url_prefix='/users')

@server.route('/login', methods=['POST'])
@cross_origin()
def login() -> str:
    result = select(request.json['email'], request.json['password'])

    if result:
        return jsonify({
            'message': 'Successfully logged in',
            'token': jwt.encode({'some': request.json['email']}, SECRET_KEY)
        }), 200
    else:
        return jsonify({
            'message': 'User not found'
        }), 400

@server.route('/register', methods=['POST'])
@cross_origin()
def register() -> str:
    result = insert(request.json['email'], request.json['password'])

    if result:
        return jsonify({
            'message': 'User created successfully',
            'token': jwt.encode({'some': request.json['email']}, SECRET_KEY)
        }), 201
    else:
        return jsonify({
            'message': 'User already exists'
        }), 400

@server.route('/delete/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id: int) -> str:
    result = remove(id)

    if result:
        return jsonify({
            'message': 'User deleted successfully'
        }), 200
    else:
        return jsonify({
            'message': 'User not found'
        }), 400
    

if __name__ == "__main__":    
    server.run(debug=True)