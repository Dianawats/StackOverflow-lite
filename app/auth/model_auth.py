"""This module handles class based views for authentication"""

import datetime
import re

import bcrypt
import jwt

from app.db.db_manager import db


class User(object):
    """
    A user class that defines a user object
    """

    def __init__(self, username, email, password_hash):
        self.user_id = 1
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_timestamp = datetime.datetime.now()

    # User password hashing
    @staticmethod
    def make_password(raw_password):
        """
        Method used to generate a hashed password
        Args:
            raw_password - Unhashed password
        """

        return bcrypt.hashpw(raw_password, bcrypt.gensalt())

    def check_password(self, raw_password):
        """
        Method used to validate password
        Args:
            raw_password  -  Unhashed password
        """
        return bcrypt.checkpw(raw_password, self.password_hash)

    # User validation
    @classmethod
    def validate_user_registration(cls, username, email, password):
        """
        Method called to create a user object
        Args:
            username {string} - username
            email {string} - email
            password_hash {string} - password
        """
        if not username or username == "" or username.isspace():
            return "username is missing, kindly provide a username"
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "email is missing/invalid email format"
        if not password or len(password) < 9:
            return "password is missing/password should be atleast 9 characters"

        return User(
            username=username, email=email,
            password_hash=User.make_password(password))

    @classmethod
    def validate_user_login(cls, username, email, password):
        """
        Method being called to validate user login
        Args:
            username {string} - username
            password_hash {string} - password
        """
        if not username or username == "" or username.isspace():
            return "username is missing, kindly provide a username"
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "email is missing/invalid email format"
        if not password or len(password) < 9:
            return "password is missing/password should be atleast 9 characters"

        return True

    # User authentication
    def generate_auth_token(self, user_id):
        """
        Method called to generate a jwt authentication
        token
        Args:
            email  -- users email
        """
        try:
            payload = {
                'exp': datetime.datetime.now() + datetime.timedelta(days=0,
                                                                    seconds=5),
                'iat': datetime.datetime.now(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                'enforcethinghow',
                algorithm='HS256'
            )

        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token):
        """
        Method called to decode a jwt user token
        This method validates the token and returns a user_id
        Args:
            token  - users token
        """
        try:
            payload = jwt.decode(token, 'enforcethinghow')
            is_token_valid = InvalidToken.is_token_valid(token)
            if not isinstance(is_token_valid, KeyError):
                return 'Token is already invalid, Please login in again'
            return payload['sub']

        except jwt.ExpiredSignatureError:
            return 'Signature expired, Please sign in again'
        except jwt.InvalidTokenError:
            return 'token is invalid, please log in again.'

    def jsonify(self):

        return {
            "username": self.username,
            "email": self.email,
            "password": self.password_hash,
            "created_at": self.created_timestamp
        }


# Invalidate user tokens
class InvalidToken(object):

    """
    Class to store invalid auth tokens
    """
    tokens = {}

    def __init__(self, token):
        self.invalidated_date = datetime.datetime.now()
        self.token = token

    @staticmethod
    def insert_invalid_token(token):
        """
        insert an invalid token into the dictionary
        returns:
        """
        InvalidToken.tokens[token] = token

    @staticmethod
    def is_token_valid(token):

        """
        Check to find out if a token has been invalidated already.
        param token: Authorization token
        returns: bool
        """
        try:
            return InvalidToken.tokens[token]

        except KeyError as e:
            return e
