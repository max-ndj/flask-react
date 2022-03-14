from flask import Flask, render_template, request, jsonify
from model import db, Users
from dotenv import load_dotenv
import os
import jwt

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET'])
def hello() -> str:
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register() -> str:
    result = Users(request.json['email'], request.json['password']).insert()

    if result:
        return jsonify({
            'status': 'success',
            'token': jwt.encode({'email': request.json['email']}, os.getenv('JWT_KEY'), algorithm='HS256').decode('utf-8')
        })
    else:
        return jsonify({
            'status': 'failed'
        })
    
@app.route('/login', methods=['POST'])
def login() -> str:
    result = Users(request.json['email'], request.json['password']).select_by_email_and_password()

    if result:
        return jsonify({
            'status': 'success',
            'token': jwt.encode({'email': request.json['email']}, os.getenv('JWT_KEY'), algorithm='HS256')
        })
    else:
        return jsonify({'status': 'failed'})

if __name__ == "__main__":
    app.run()