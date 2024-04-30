from flask_testing import TestCase
from flask import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))


from ....app import create_app

class TestRuleBasedParaphrase(TestCase):
    
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app
    
    def test_paraphrase(self):
        data = {"input": "Example text"}
        response = self.client.post('/V1/paraphrase/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('paraphrase', json.loads(response.data.decode()))
