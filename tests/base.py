import unittest
import json
from app import create_app
from app.config import TestingConfig


class BaseTestCase(unittest.TestCase):
    """Initialises a base class
    Args:
        unittest {[type]} -- [description]
    Returns:
        [type] -- [description]
    """

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

    def create_question(self):
        """
        Method that sends a POST request to create a question object
        """
        return self.client.post(
            '/api/v1/questions', content_type='application/json',
            data=json.dumps(dict(title="python",
                            body="python is a good OOP lang", tag="python3")))

    def create_creation_with_missing_attributes(self):
        """
        Method that sends a post request to create a question object
        with missing required parameters.
        """
        return self.client.post(
            '/api/v1/questions', content_type='application/json',
            data=json.dumps(dict(title="Python",
                            body="python is a good OOP lang")))

    def get_all_questions(self):
        """
        Method to send a get request to fetch all question objects
        """
        return self.client.get(
             '/api/v1/questions', content_type='application/json')
