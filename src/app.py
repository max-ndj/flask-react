from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate
from config import SECRET_KEY
from controllers.UserController import select, insert, remove
from models.User import db
from routes.user_bp import user_bp
import jwt

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/', methods=['GET'])
def hello() -> str:
    return render_template('index.html')

@app.route('/login', methods=['POST'])
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

@app.route('/register', methods=['POST'])
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

@app.route('/delete/<int:id>', methods=['DELETE'])
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
    app.run(debug=True)