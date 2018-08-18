import app
import unittest
import json


class ApiTestCase(unittest.TestCase):
    """This class represents the Api test case
       Testing question and asnwer
    """

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.mock_data = {
            'id',
            'question': 'How do I use oop'
                          }
        self.answer = {
            'answer': 'aswering question above'
                          }

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        res = self.client().post('/questions/', data=self.question)
        self.assertEqual(res.status_code, 201)
        self.assertIn('python programming', str(res.data))

    def test_api_can_get_all_questions(self):
        """Test API can get a question (GET request)."""
        res = self.client().post('/questions/', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/questions/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('python programming', str(res.data))
      
    def test_api_can_get_question_by_id(self):
        """Test API can get a single question by using it's id."""
        
        rv = self.client().post('/questions/', data=self.question)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/answers/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('java is cool right?', str(result.data))

    def tearDown(self):
                """teardown configs after running tests"""
                 

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()



