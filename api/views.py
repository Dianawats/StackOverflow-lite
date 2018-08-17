"""
    api.views
    ~~~~~~~~~~~
    This module provides class-based views inspired by the ones in flask.
    """

from flask import Flask, request, jsonify, make_response
from.models import Questions

# registering the application name
app = Flask(__name__)

# question object is being initiates
questionsObj = Questions()
questions = questionsObj.list_of_question()

@app.route('/')
def index():
    """Homepage by default"""
    return "Endpoints using flask"


def _get_question(question_id):
    """
    protected method that returns id args 
    and passed param (int): question_id
     then returns id
    """
    return[question for question in questions
           if question['question_id'] == question_id]


def _find_question(question_name):
    """
    protected method that returns the question
    Args:
        param (question_name): Question name
    Returns:
        question_name
    """
    return next(filter(lambda q: q['question_name'] == question_name,
                questions), None)

@app.errorhandler(404)
def not_found(error):
    """
    Request Not Found and returns the error
    Args:
        param (error): error
    Returns:
        404
    """
    return make_response(jsonify({'error': 'Question Not Found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    """
    No response from the server because of bad request
    Args:
        param (error): error
    Returns status code:
        400, badrequest error
    """
    return make_response(jsonify({'error': 'No question found'}), 400)


@app.errorhandler(409)
def question_exist(error):
    """
    Question is existing, the request is conflicting 
    Args:
        param (error): error
    Returns:
        conflicts, 409
    """
    return make_response(jsonify({'error': 'the question has been created'}),
                         409)


@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    """
    fetch all questions from the model
    Args:
        None
    Returns:
        questions, ok
    """
    return jsonify({'questions': questions}), 200
