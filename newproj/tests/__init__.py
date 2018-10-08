import unittest
from run import app


class BaseTestCase(unittest.TestCase):
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
        
def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()