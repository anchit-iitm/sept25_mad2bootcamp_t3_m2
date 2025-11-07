from flask import request, jsonify, make_response
from flask_restful import Resource

from models import Person


class users(Resource):

    def get(self):
        users = Person.get_all()
        return make_response(jsonify({"data": users, "message": "Users retrieved successfully"}), 200) if users else make_response(jsonify({"message": "No users found"}), 404)
    
    def post(self):
        data = request.json
        new_user = Person.create(data.get('name'), data.get('age'))
        return make_response(jsonify({"data": new_user, "message": "User created successfully"}), 201) if new_user else make_response(jsonify({"message": "Invalid data"}), 422)
    
    def put(self):
        data = request.json
        updated_user = Person.update(data.get('id'), data.get('name'), data.get('age'))
        return make_response(jsonify({"data": updated_user, "message": "User updated successfully"}), 202) if updated_user else make_response(jsonify({"message": "User not found"}), 404)

    def delete(self):
        data = request.json
        deleted_user = Person.delete(data.get('id'))
        return make_response(jsonify({"data":deleted_user, "message": "User deleted successfully"}), 202) if deleted_user else make_response(jsonify({"message": "User not found"}), 404)