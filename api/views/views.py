"""
    api.views
    ~~~~~~~~~~~

    This module provides class-based views inspired by the ones in flask.
    """

from flask import Flask, jsonify, abort, request, make_response, url_for
from api.models.models import Questions

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
    protected method that returns id
    Args:
        param (int): question_id
    Returns:
        id
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
    Request Not Found
    Args:
        param (error): error
    Returns:
        404
    """
    return make_response(jsonify({'error': 'Question Not Found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    """
    Server fails to make a respond due to bad request
    Args:
        param (error): error
    Returns:
        400
    """
    return make_response(jsonify({'error': 'No question found'}), 400)


@app.errorhandler(409)
def question_exist(error):
    """
    Conflicting request, question exist
    Args:
        param (error): error
    Returns:
        conflicts, 409
    """
    return make_response(jsonify({'error': 'Already Created the question'}), 409)


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
def ask_question():
    """
    Creates question from request object (from user)
    Args:
        None
    Returns:
        created, 201
    """
    if not request.json or 'question_class' not in request.json \
            or 'question_name' not in request.json:
        abort(400)

    question_id = questions[-1].get('question_id') + 1
    question_class = request.json.get('question_class')
    question_name = request.json.get('question_name')

    asked_question = _find_question(question_name)
    if asked_question is not None:
        abort(409)

    question = {
        'question_id': question_id,
        'question_class': question_class,
        'question_name': question_name,
        'answer': []
    }

    questions.append(question)
    return jsonify({'question': question}), 201
    
# @app.route('/api/v1/questions', methods=['GET'])
# def get_questions():
#     return jsonify({'questions': questions})


# @app.route('/api/v1/questions/<int:question_id>', methods=['GET'])
# def get_question(question_id):
#     question = [question for question in questions if question['id'] 
#      == question_id]
#     if len(question) == 0:
#         abort(404)
#     return jsonify({'question': question[0]})


# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)


# @app.route('/api/v1/questions', methods=['POST'])
# def create_question():
#     if not request.json or not'title' in request.json:
#         abort(400)
#     question = {
#         'id': questions[-1]['id'] + 1,
#         'title': request.json['title'],
#         'question_body': request.json.get('question_body', ""),
#         'question_tag': request.json.get('question_tag', "")
#     }
#     questions.append(question)
#     return jsonify({['question']}), 201


# @app.route('/api/v1/questions/<int:question_id>/answers', methods=['POST'])
# def post_question(question_id):
#     question = [question for question in questions if question['id'] 
#         == question_id]
#     if len(question) == 0:
#         abort(404)
#     return jsonify({'question': question[0]})


# @app.route('/api/v1/questions/<int:question_id>', methods=['PUT'])
# def update_question(question_id):
#     question = [question for question in questions if 
#                 question['id'] == question_id]
#     if len(question) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'title' in request.json and type(request.json['title']) != unicode:
#         abort(400)
#     if 'question_body' in request.json and type(request.json['question_body']) is not unicode:
#         abort(400)
#     question[0]['title'] = request.json.get('title', question[0]['title'])
#     question[0]['question_body'] = request.json.get('question_body',
#                                                      question[0]['question_body'])
#     question[0]['question_tag'] = request.json.get('question_tag', question[0][
#                                                    'question_tag'])
#     return jsonify({'question': question[0]})


# @app.route('/api/v1/questions/<int:question_id>', methods=['DELETE'])
# def delete_question(question_id):
#     question = [question for question in questions if question['id'] 
#                           == question_id]
#     if len(question) == 0:
#         abort(404)
#     questions.remove(question[0])
#     return jsonify({'result': True})