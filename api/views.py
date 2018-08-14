"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.
    """

from flask import Flask
from models import Questions

app = Flask(__name__)
# question object is being initiates
questionsObj = Questions()
questions = questionsObj.list_of_question()

