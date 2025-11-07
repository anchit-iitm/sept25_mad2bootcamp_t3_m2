from flask import jsonify, make_response
from flask_restful import Resource



# @bp_app.route('/', methods=['GET'])
# def home():
class home(Resource):
    def get(self):
        return "Welcome to the LookBack App!"

class about(Resource):
    def get(self):
        return {"message": "This is the About page of the LookBack App!", "status": "success"}