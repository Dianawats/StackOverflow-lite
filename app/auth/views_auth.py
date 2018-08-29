from flask import Blueprint, jsonify, request
from flask.views import MethodView
from app.auth.auth_handlers import check_for_user_key_error
from app.auth.auth_handlers import response_for_get_all_users
from app.auth.auth_handlers import response
from app.auth.auth_handlers import convert_list_to_json
from app.auth.auth_handlers import auth_success_response
from app.auth.model_auth_controller import user_controller
# from app.auth.auth_model_controller import token_controller
from app.auth.model_auth import User, InvalidToken


auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1')


class SignUp(MethodView):
    """
    class signup 
    """
    methods = ['POST', 'GET']

    def post(self):
        if not request.content_type == 'application/json':
            return response('request must be in json format', 'failed', 400)

        sent_data = request.get_json()
        username = sent_data.get('username')
        email = sent_data.get('email')
        password = sent_data.get('password')

        user = User.validate_user_registration(
            username=username, email=email, password=password)
        if not isinstance(user, User):
            return response(user, 'failed', 400)
                                                                                                                                           
        ext_user = user_controller.check_if_user_exists(email)
        if not isinstance(ext_user, bool):
            return response(ext_user, 'failed', 400)

        user_controller.insert_user(user)
        token = user.generate_auth_token(user.user_id)
        if not isinstance(token, bytes):
            return response(str(token), 'failed', 400)

        return auth_success_response(
            user.username + ' has signed up',
            token, 'success', 201
        )


class Login(MethodView):
    """
    login class
    """

    def post(self):
        
        if not request.content_type == 'application/json':
            return response('request must be in json format', 'failed', 400)

        sent_data = request.get_json()
        username = sent_data.get('username')
        email = sent_data.get('email')
        password = sent_data.get('password')

        respo = User.validate_user_login(
            username=username, email=email, password=password)

        if not isinstance(respo, bool):
            return response(respo, 'failed', 400)

        user = user_controller.get_user_by_email(email)
        print(user)
        message = check_for_user_key_error(user)
        if message:
            return response(message, 'failed', 400)

        if not user.check_password(password):
            return response('password provided is incorrect', 'failed', 400)

        token = user.generate_auth_token(user.user_id)
        if not isinstance(token, bytes):
            return response(str(token), 'failed', 400)
        return auth_success_response(
           user.username + ' is now logged in',
           token, 'success', 200
        )


class Logout(MethodView):
    """
    logout class
    """

    def post(self):

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return response('Provide an authorization header', 'failed', 403)
        try:
            auth_token = auth_header.split(" ")[1]

        except IndexError:
            return response('failed to index token', 'failed', 403)
        else:
            decoded_token_response = User.decode_auth_token(auth_token)
            if not isinstance(decoded_token_response, int):
                return response(str(decoded_token_response), 'failed', 401)
            token = InvalidToken(auth_token)
            InvalidToken.insert_invalid_token(token)
            return response('successfully logged out', 'success', 200)


# Register a class as a view
signup = SignUp.as_view('register')
login = Login.as_view('login')
logout = Logout.as_view('logout')


# Add url_rules for the API endpoints
auth_bp.add_url_rule('/auth/signup', view_func=signup)
auth_bp.add_url_rule('/auth/login', view_func=login)
auth_bp.add_url_rule('/auth/logout', view_func=logout)
