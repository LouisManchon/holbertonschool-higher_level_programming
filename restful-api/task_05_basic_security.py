from flask import Flask, jsonify, request

from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'ton_super_secret_jwt_key'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def check_pass(username, password):
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def login():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def login_jwt():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"message": "username and password required"}), 400

    if check_pass(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run()
