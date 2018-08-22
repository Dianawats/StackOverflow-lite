import unittest
from tests.base import BaseTestCase
from app.models.models import Question, Answer


class TestDataModels(BaseTestCase):
    """
     Initialises class Data models for data models testing
    Args:
     BaseTestCase {Class} -- Base test class for running custom tests
    """

    def test_question_model(self):
        """
        Method that tests question model instance
        """

        question_1 = Question('Checking',
                              'check whether verything s ok',
                              'pytest')
        self.assertIsInstance(question_1, Question)
        self.assertTrue(question_1.title, 'Checking')
        self.assertTrue(
            question_1.body, 'check whether verything s ok')
        self.assertTrue(question_1.tag, 'pytest')

    def test_answer_model(self):
        """
         Method that tests Answer model instance
        """
        answer_1 = Answer(1, 'answer to the question one')
        self.assertIsInstance(answer_1, Answer)
        self.assertTrue(answer_1.body, 'answer to the question one')
        self.assertEqual(answer_1.id, 1)
