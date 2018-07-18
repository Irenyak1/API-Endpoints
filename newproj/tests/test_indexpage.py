import json
from tests import BaseTestCase

class ApiTestcase(BaseTestCase):
        
    def test_can_return_indexpage(self):
        response = self.test_client.get('/')
        self.assertEqual(response.status_code, 200 )
        self.assertIn('index.html', response.data.decode())

