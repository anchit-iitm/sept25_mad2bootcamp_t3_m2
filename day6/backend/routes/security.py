from flask import jsonify, make_response, request

from .import bp_app
from models import user_datastore, db
from security import hash_password, verify_password

@bp_app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    email = data.get('email')

    password = data.get('password')

    if not email or not password:
        return make_response(jsonify({"error": "Email and password are required."}), 400)

    existing_user = user_datastore.find_user(email=email)
    if existing_user:
        return make_response(jsonify({"error": "User already exists."}), 400)
    hashed_password, status = hash_password(password)
    if status == False:
        return make_response(jsonify({"error": "Some unexpected error occured"}), 500)
    new_user = user_datastore.create_user(email=email, password=hashed_password)
    user_datastore.add_role_to_user(new_user, 'user')
    db.session.commit()
    return make_response(jsonify({"message": "User registered successfully.", "user_id": new_user.id}), 201)

@bp_app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return make_response(jsonify({"error": "Email and password are required."}), 400)

    user = user_datastore.find_user(email=email)
    status = True
    if not verify_password(user.password, password):
        status = False
    if not user or not status or not user.active:
        return make_response(jsonify({"error": "please use correct credentials, or contact admin"}), 401)
    
    return make_response(jsonify({"message": "Login successful.", "user_id": user.id, 'authToken': user.get_auth_token()}), 200)