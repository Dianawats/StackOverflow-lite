"""
    api.views
    ~~~~~~~~~~~
    This module provides class-based views inspired by the ones in flask.
    """

from flask import request, jsonify, make_response, abort
from api import app
from api.models import questions
from api.models import answers

# question object is being initiated
questions = questions.list_of_question()
# access the method of class Answers
answers = answers.list_of_answer()


@app.route('/')
def index():
    """Homepage by default"""
    return "Testing the apis endpoints"


def _get_question(question_id):
    """
    protected method that returns id args 
    and passed param (int): question_id
     then returns id
    """
    return[question for question in questions
           if question['question_id'] == question_id]


def _find_question(question_title):
    """
    protected method that returns the question
    Args:
        param (question_title): Question name
    Returns:
        question_title
    """
    return next(filter(lambda q: q['question_title'] == question_title,
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
    the server won't respond because of bad request
    Args:
        param (error): error
    Returns status code:
        400, badrequest error
    """
    return make_response(jsonify({'error': 'No question found'}), 400)


@app.errorhandler(409)
def question_exist(error):
    """
    Question is existing, the request is conflicting: 
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


@app.route('/api/v1/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """
    Returns specific question given id
    Args:
        param (int): question id
    Returns:
        question, ok
    """
    question = _get_question(question_id)
    if not question:
        abort(404)
    return jsonify({'question': question}), 200


@app.route('/api/v1/questions', methods=['POST'])
def create_question():
    """
    Args: None
    If the data isn't there, or if it is there, but we are missing a title item
    returns: 400, bad request
    We append the new question to our questions array,
    then respond to the client with the added question,
    send back a status code 201, "Created"

    """
    if not request.json or not'title' in request.json:
        abort(400)
    question = {
        'id': questions[-1]['id'] + 1,
        'title': request.json['title'],
        'question_body': request.json.get('question_body', ""),
        'question_tag': request.json.get('question_tag', "")
    }
    questions.append(question)
    return jsonify({['question']}), 201


@app.route('/api/v1/questions/<int:question_id>/answers', methods=['POST'])
def add_answer(question_id):
    if not request.json or 'answer_body' not in request.json:
        abort(400)

    if _get_question(question_id) is False:
        abort(404)

    for question in questions:
        for key, value in question.items():
            question = question
            break

    last_id = 0

    if len(answers) > 0:
        last_id = answers[-1].get('answer_id')

    answer_id = last_id + 1
    question_id = _get_question(question_id)['question_id']
    answer_body = request.json.get('answer_body')

    answer = {
        'answer_id': answer_id,
        'question_id': question_id,
        'answer_body': answer_body
    }

    answers.append(answer)
    return jsonify({'answer': answer}), 201  
