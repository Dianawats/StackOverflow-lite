import app
import unittest
import json
from api import views
from copy import deepcopy


DEFAULT_URL = 'http://127.0.0.1:5000/api/v1/questions'
GOOD_URL = '{}/2'.format(DEFAULT_URL)
BAD_URL = '{}/3'.format(DEFAULT_URL)
ANSWER_URL = '{}/2/answers'.format(DEFAULT_URL)


class ApiTestCase(unittest.TestCase):
    """This class represents the Api test case
       Testing question and asnwer
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.questionCopy = deepcopy(views.questions)
        self.answerCopy = deepcopy(views.answers)
        self.app = app.app.test_client()
        self.app.testing = True

    def test_api_can_get_all_questions(self):
        """Test API can get a question (GET request)."""
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(len(data['questions']), 2)
        self.assertEqual(res.status_code, 200)
        
    def test_api_get_single_question(self):
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(data['questions'][0]['question_title'], 
                         'Datatypes-boolean')
        self.assertEqual(res.status_code, 200)

    def test_api_can_post_answer(self):
        answer = {
            'answer_body': 'java is also an OOP programming language'
        }
        res = self.app.post(ANSWER_URL,
                            data=json.dumps(answer),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_api_can_add_question(self):
        question = {
            'question_title': 'Java',
            'question_body': 'how to write a method using hibernate'
        }
        res = self.app.post(DEFAULT_URL,
                            data=json.dumps(question),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_api_bad_request_question(self):
        question = {
            'question_title': 'python',
            'question_body': 'How do I configure the server'
        }
        res = self.app.post(DEFAULT_URL,
                            data=json.dumps(question),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def tearDown(self):
        """teardown configuratios after running tests
        """
        views.questions = self.questionCopy
        views.answers = self.answerCopy

                
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
