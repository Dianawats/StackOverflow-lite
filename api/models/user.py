import re
from api.models.user import Users
from api import generate_id

users_list = []
user_id = generate_id(users_list)


class User(object):
    """Creating a class for the user model
    """

    def __init__(self, user_id, first_name, last_name, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @property
    def first_name(self):
        return self._first_name
        
    @first_name.setter
    def first_name(self, value):
        if not value:
            raise Exception("the field can't be null")
        if len(value) <= 2:
            raise Exception("the first name is very short")
        if re.compile('[!@#$%^&*:;?><.0-8]').match(value):
            raise ValueError("not permitted xters are invalid")

        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
        
    @last_name.setter
    def last_name(self, value):
        if not value:
            raise Exception("the field can't be null")
        if len(value) <= 2:
            raise Exception("the last name is very short")
        if re.compile('[!@#$%^&*:;?><.0-8]').match(value):
            raise ValueError("not permitted xters are invalid")

        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise Exception("Email field cannot be None")
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", value):
            raise ValueError('Enter the Valid Email')
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        if not pwd:
            raise Exception("Field cannot be None")
        if len(pwd) < 6 and len(pwd) > 14:
            raise Exception(
                "Weak password \n Password must be atleast 6 characters long ")
        if not re.search(r'[0-15]', pwd):
            raise Exception(
                'Weak password \n Password should contain atleast one number')
        if pwd.isupper() or pwd.islower() or pwd.isdigit():
            print(
                "Weak password \n Either you have to add alphabets or \
                 try to apply both letter cases")
        self._password = pwd

      
