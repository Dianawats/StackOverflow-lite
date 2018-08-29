import datetime

"""This module handles database queries"""


class Question:
    """
    This class defines Question Model
    """

    def __init__(self,author, title, body, tag):
        """Initializes the question object"""
        self.id = 0
        self.author = author
        self.posted_date = datetime.datetime.now()
        self.title = title
        self.body = body
        self.tag = tag
        self.answers = []

    def jsonify(self):
        return {
            "id": self.id,
            "author": self.author,
            "date_posted": self.posted_date,
            "title": self.title,
            "body": self.body,
            "tag": self.tag,
            "answers": self.answers
        }
    

class Answers:
    """
    Answer Model
    """
    def __init__(self, ans_id, body):
        self.id = ans_id
        self.author = "Dian"
        self.body = body
        self.posted_date = datetime.datetime.now()
        self.accepted = False
        self.comments = []
        self.votes = []

    def make_json(self):
        return {
            "qtn_id": self.id,
            "author": self.author,
            "body": self.body,
            "date_posted": self.posted_date,
            "accepted": self.accepted,
            "comments": self.comments,
            "votes": self.votes
        }


class Comment(object):
    """
    Comment Model
    """
    def __init__(self, username, body, id):
        self.username = username
        self.body = body
        self.id = id
        self.status = 'PUBLIC'
        self.created_timestamp = datetime.datetime.now()

    def make_json(self):
        return {
            "ans_id": self.id,
            "username": self.username,
            "status": self.status,
            "body": self.body,
            "date_posted": self.created_timestamp
        }



class Tag(object):
    def __init__(self, name):
        self.name = name