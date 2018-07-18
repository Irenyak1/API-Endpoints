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
    
    def test_can_fetch_users(self):
        response = self.test_client.get('/users')
        self.assertEqual(response.status_code, 200 )
        self.assertIn("users", response.data.decode())
    
    



