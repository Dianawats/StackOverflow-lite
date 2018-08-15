from flask import Blueprint, request, jsonify, make_response
from api.models.user import User, users_list

auth = Blueprint('auth', __name__)


@auth.route('/api/v1/users/signup', methods=['POST'])
def register():
    if not request.get_json():
        return make_response(jsonify({"message": "Request should return json"}),400)
    email = request.get_json()['email']
    password = request.get_json()['password']

    user = {
        'email': email,
        'password': password
    }

    User('user_id', email=email, password=password)

    for user in users_lists:
        if email == user["email"]:
            return make_response(jsonify({'message': Email already exist}))
    users_list.append(user)

    return jsonify(user), 201
