"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.
    """

from flask import Flask, request, jsonify, make_response, abort
from .models import Questions

# registering the application name
app = Flask(__name__)
# question object is being initiates
questionsObj = Questions()
questions = questionsObj.list_of_question()


@app.route('/')
def index():
    """Homepage by default"""
    return "Endpoints using flask"


@app.route('/api/v1/questions', methods=['GET'])
"""Creating a get question function, that is 
associated with the URI and only for GET http method
and returns JSON data
"""
def get_questions():
    return jsonify({'questions': questions})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1/questions', methods=['POST'])
