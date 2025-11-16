from flask import request, jsonify, make_response
from flask_security import auth_required
from .import bp_app


@bp_app.route('/')
def home():
    return "Welcome to the LookBack App!"
@bp_app.route('/about')
# @auth_required('token')
def about():
    return {"message": "This is the About page of the LookBack App!", "status": "success"}, 200