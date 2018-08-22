import unittest
import json
from tests.base import BaseTestCase


class TestAnswerView(BaseTestCase):
    """
    Testing for AnswerView Method View Class

    Args:
        Base test class for running custom tests
    """
    # POST AN ANSWER

    def test_create_an_answer(self):
        """
       Method that tests successful POST request to
        create an answer for a specific question
        """
        with self.client:
            # post a question
            post_resp = self.create_question()
            self.assertEqual(post_resp.status_code, 201)

            # post an answer
            response = self.client.post(
                '/api/v1/questions/1/answers',
                content_type='application/json',
                data=json.dumps(dict(body='answer body'))
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertTrue(data['status'], 'success')
            self.assertTrue(data['id'], 1)
            self.assertTrue(data['body'], 'answer body')
            self.assertIsInstance(data['answers'], list)

    def test_create_answer_with_wrong_content_type(self):
        """
        Method Testing unsuccessful POST request to
        create an answer with content_type not of json format
        """
        with self.client:
            response = self.client.post(
                '/api/v1/questions/1/answers',
                content_type="xml",
                data=json.dumps(dict(body='answer body'))
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'request must be of json format')
            self.assertTrue(data['status'], 'failed')

    
