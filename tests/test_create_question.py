import unittest
import json
from tests.base import BaseTestCase


class TestCreateQuestion(BaseTestCase):
    """
    Testing for QuestionsView Method View Class
    Arg:
    Base test class for running custom tests
    """
    # this class tests a question creation

    def test_create_a_question(self):
        """
        Ihis method tests a successful post request to create a question
        """
        with self.client:
            response = self.create_question()

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertTrue(data['status'], 'success')
            self.assertTrue(data['id'], 1)
            self.assertTrue(data['body'], "python is a good OOP lang")
            self.assertIsInstance(data['answers'], list)

    def test_create_question_with_a_missing_attribute(self):
        """
        This method tests unsuccessful post request to
        create a question when missing some required fields
        """
        with self.client:
            response = self.create_creation_with_missing_attributes()

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'missing required parameter')
            self.assertTrue(data['status'], 'failed')

    def test_create_question_with_wrong_content_type(self):
        """
        Method that tests unsuccessful post request to
        create a question with wrong content type
        """
        with self.client:
            response = self.client.post(
                '/api/v1/questions',
                content_type="xml",
                data=json.dumps(dict(title='Python',
                                     body='python is a good OOP lang', 
                                     tag='Python3'))
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'request must be of json format')
            self.assertTrue(data['status'], 'failed')
