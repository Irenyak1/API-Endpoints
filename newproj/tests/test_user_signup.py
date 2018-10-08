import json
from tests import BaseTestCase
from api import app

class ApiTestcase(BaseTestCase):
    def setUp(self):
        self.user = {
            "name": "Moses Tete",
            "username": "wango",
            "email": "galiwango@gmail.com",
            "password": "kabulasoke1",
            "confirmation": "kabulasoke1"
        }
        self.content_type="application/json"
        self.test_client = app.test_client()

    def test_can_create_user(self):
        user_data = json.dumps(self.user)
        response = self.test_client.post('/users', data=user_data, content_type=self.content_type)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data.decode())
        self.assertEqual(self.user, response_data.get('user'))
    
    
    def test_cant_create_a_user(self):
        """ Tests whether a user cant create an account if no email sent"""
        invalid_user = json.dumps({"username":"wango", "password":"password"})
        response = self.test_client.post('/users', data=invalid_user, content_type=self.content_type)
        self.assertTrue(response.status_code == 422)
        self.assertIn("Email is required",response.data.decode())