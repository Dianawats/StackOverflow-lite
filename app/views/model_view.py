from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.models.models import Question, Answer
from app.models.model_controller import question_controller
from app.response_handlers import response
from app.response_handlers import response_for_returning_single_question
from app.response_handlers import convert_list_to_json
from app.response_handlers import response_for_get_all_questions
from app.response_handlers import response_to_fetch_single_question
from app.response_handlers import response_for_get_all_answers
from app.response_handlers import convert_user_answers_list_to_json


qtn_bp = Blueprint('question', __name__, url_prefix='/api/v1')


# This method is a helper function
def check_for_key_error(resp):
    """
    This function is used to return a custom response
     if an out of index error is popped.

    Args:
        resp -- object returned from the request
    """
    if isinstance(resp, KeyError):
            return 'Question ' + str(resp) + ' does not exist'


class QuestionsView(MethodView):

    methods = ['POST', 'GET']

    def post(self):
        """
        This method initialises post request to create a question
        """

        if not request.content_type == 'application/json':
            return response('request should be of json format', 'failed', 400)

        sent_data = request.get_json()
        title = sent_data.get('title')
        body = sent_data.get('body')
        tag = sent_data.get('tag')

        if not title or not body or not tag:
            return response('required parameter is missing', 'failed', 400)

        question = Question(title=title, body=body, tag=tag)
        question_controller.insert_question(question)
        return response_for_returning_single_question(
            question, 201)

    def get(self):
        """
        This method defines GET request to fetch all questions
        """

        if not request.content_type == 'application/json':
            return response('request should be of json format', 'failed', 400)

        questions = question_controller.get_all_questions()
        return response_for_get_all_questions(
            convert_list_to_json(questions), 200)


class QuestionView(MethodView):

    methods = ['GET']

    def get(self, qtn_id):
        """
        Method get request to get a question by id
        """
        if not request.content_type == 'application/json':
            return response('request should be of json format', 'failed', 400)

        resp = question_controller.get_question(qtn_id)
        message = check_for_key_error(resp)
        if message:
            return response(message, 'failed', 400)
        return response_to_fetch_single_question(resp.jsonify(), 200)


class AnswerView(MethodView):

    methods = ['POST', 'GET']

    def post(self, qtn_id):
        """
        This method post request to create an answer to a particular question

        Args:
            MethodView {[type]} -- [descriptison]
            qtn {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request should be of json format', 'failed', 400)

        sent_data = request.get_json()
        body = sent_data.get('body')
        respon = question_controller.get_question(qtn_id)
        message = check_for_key_error(respon)
        if message:
            return response(message, 'failed', 400)

        answer = Answer(respon.id, body=body)
        respon.answers.append(answer.make_json())
        return response_for_returning_single_question(respon, 201)

    def get(self, qtn_id):
        """
        Method GET request to fetch all answers for a particular question

        Args:
            qtn_id {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request should be of json format', 'failed', 400)

        respons = question_controller.get_question(qtn_id)
        message = check_for_key_error(respons)
        if message:
            return response(message, 'failed', 400)

        answers = convert_user_answers_list_to_json(respons.answers)
        return response_for_get_all_answers(answers, 200)


# Register a class as a view
question_list = QuestionsView.as_view('questions')
question = QuestionView.as_view('question')
answer = AnswerView.as_view('answer')


# Adding url_rules for our API endpoints
qtn_bp.add_url_rule('/questions', view_func=question_list)
qtn_bp.add_url_rule('/questions/<int:qtn_id>', view_func=question)
qtn_bp.add_url_rule('/questions/<int:qtn_id>/answers', view_func=answer)

