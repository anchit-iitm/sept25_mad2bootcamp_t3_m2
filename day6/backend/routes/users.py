from flask import request, jsonify, make_response
from flask_security import auth_required, roles_required
from .import bp_app
from caching import cache


@bp_app.route('/users', methods=['POST', 'PUT', 'DELETE'])
@auth_required('token')
@roles_required('admin')
def users():
    from models import Person

    
    if request.method == 'POST':
        data = request.json
        new_user = Person.create(data.get('name'), data.get('age', 0)) #data['name'], data['age']
        return make_response(jsonify({"data": new_user, "message": "User created successfully"}), 201) if new_user else make_response(jsonify({"message": "Invalid data"}), 422)
    
    if request.method == 'PUT':
        data = request.json
        updated_user = Person.update(data.get('id'), data.get('name'), data.get('age'))
        # i can delete the cache for all users here
        return make_response(jsonify({"data": updated_user, "message": "User updated successfully"}), 202) if updated_user else make_response(jsonify({"message": "User not found"}), 404)

    if request.method == 'DELETE':
        data = request.headers.get('id')
        print(data, type(data))
        deleted_user = Person.delete(int(data))
        return make_response(jsonify({"data":deleted_user, "message": "User deleted successfully"}), 202) if deleted_user else make_response(jsonify({"message": "User not found"}), 404)
    

@bp_app.route('/user', methods=['GET'])
@auth_required('token')
@roles_required('admin')
@cache.cached(timeout=25, key_prefix='all_users')
def user():
    from models import Person
    if request.method == 'GET':
        users = Person.get_all()
        return make_response(jsonify({"data": users, "message": "Users retrieved successfully"}), 200) if users else make_response(jsonify({"message": "No users found"}), 404)