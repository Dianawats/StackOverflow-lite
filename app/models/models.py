
"""This module handles database queries"""


class User:
    """This class does all database related stuff for the user"""

    def __init__(self, user_id, name, username, password):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password


class Question:
    """
    This class defines Question Model
    """

    def __init__(self, title, body, tag):
        """Initializes the question object"""
        self.question_id = id
        self.title = title
        self.body = body
        self.tag = tag


class Answers:
    """
    Answer Model
    """
    def __init__(self, ans_id, body):
        self.id = ans_id
        self.body = body


