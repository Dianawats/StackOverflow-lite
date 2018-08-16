from flask import Blueprint, request, jsonify, make_response
from api.models.user import User, users_list

auth = Blueprint('auth', __name__)


@auth.route('/api/v1/users/signup', methods=['POST'])
def register():
    if not request.get_json():
        return make_response(jsonify({"message": "Request should return json"}), 
                             400)
    user_name = request.get_json()['user_name']
    email = request.get_json()['email']
    password = request.get_json()['password']

    user = {
        'user': user_name,
        'email': email,
        'password': password
    }

    User('user_id', user_name=user_name, email=email, password=password)

    for user in users_list:
        if email == user["email"] and user_name == user["user_name"]:
            return make_response(jsonify({'message': 'Email already exists'}))
        elif user_name == user["user_name"]:
            return make_response(jsonify({'message': 'User exists already'}))
    users_list.append(user)

    return jsonify(user), 201
