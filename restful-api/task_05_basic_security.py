from flask import Flask, jsonify, request

from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = "secret-password-key"
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


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return 'JWT Auth: Access Granted'

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def access_admin():
    current_user = get_jwt_identity()
    if current_user not in users:
        return jsonify({"error": "Invalid token"}), 401

    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
