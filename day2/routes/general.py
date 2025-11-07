from flask import request, jsonify, make_response

from .import bp_app


@bp_app.route('/')
def home():
    return "Welcome to the LookBack App!"
    
@bp_app.route('/about')
def about():
    return {"message": "This is the About page of the LookBack App!", "status": "success"}