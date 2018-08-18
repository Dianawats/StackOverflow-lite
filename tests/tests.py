import app
import unittest
import json
from api import views
from copy import deepcopy


DEFAULT_URL = 'http://127.0.0.1:5000/api/v1/questions'
GOOD_URL = '{}/2'.format(DEFAULT_URL)
BAD_URL = '{}/3'.format(DEFAULT_URL)
ANSWER_URL = '{}/2/answers'.format(DEFAULT_URL)
NO_QUESTION_URL = '{}/3/answers'.format(DEFAULT_URL)


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
        
    def test_get_single_question(self):
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(data['questions'][0]['question_title'], 
                         'Datatypes-boolean')
        self.assertEqual(res.status_code, 200)

    def test_post_answer(self):
        answer = {
            'answer_body': 'java is also an OOP programming language'
        }
        res = self.app.post(ANSWER_URL,
                            data=json.dumps(answer),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_add_question(self):
        question = {
            'question_body': 'how to write a method using hibernate',
            'question_tag': 'java?'
        }
        res = self.app.post(DEFAULT_URL,
                            data=json.dumps(question),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    # def test_question_creation(self):
    #     """Test API can create a question (POST request)"""
    #     res = self.app.get(DEFAULT_URL)
    #     self.assertEqual(res.status_code, 201)
    #     self.assertIn('Datatypes-boolean', str(res.data))

    def test_api_can_get_all_questions(self):
        """Test API can get a question (GET request)."""
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(len(data['questions']), 2)
        self.assertEqual(res.status_code, 200)

    def test_question_as_answer(self):
        res = self.app.get(GOOD_URL)
        data = json.loads(res.get_data())
        self.assertEqual(len(data['answers']), 3)
        self.assertEqual(res.status_code, 200)
 
    def tearDown(self):
        """teardown configs after running tests
            Method to tidy up lists after the test is run
        """
        views.questions = self.questionCopy
        views.answers = self.answerCopy

                
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()



