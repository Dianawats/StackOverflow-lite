from app.auth.model_auth import User
from app.auth.model_auth import InvalidToken


class UserController(object):
    """
    Controller class for handling and storing user data
    """
    def __init__(self):
        self.users = {}

    # check if user exits based on an email address
    def check_if_user_exists(self, email):

        try:
            self.users[email]
            return 'user with ' + email + ' already exists'

        except KeyError:

            return False

    def insert_user(self, user):
        self.users[user.email] = user

    def get_user_by_email(self, email):

        try:
            return self.users[email]

        except KeyError as e:
            return e

    def get_all_users(self):
        return [v for v in self.users.values()]


class TokenController(object):
    """
    Controller class for handling and storing invalid tokens
    """
    def __init__(self):
        self.tokens = {}

    def insert_invalid_token(self, token):
        """
        insert an invalid token into the dictionary
        returns:
        """
        self.tokens[token] = token

    def is_token_valid(self, token):

        """
        Check to find out whether a token has already been invalidated.
        param token: Authorization token
        returns: bool
        """
        try:
            return self.tokens[token]

        except KeyError as e:
            return e

# A user controller instance
user_controller = UserController()


# A user controller instance
token_controller = TokenController()
