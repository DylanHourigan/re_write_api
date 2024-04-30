from flask_testing import TestCase
from flask import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))


from ....app import create_app

class TestPreTrainedParaphrase(TestCase):
    
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_paraphrase_single(self):
        data = {"input": "Example text"}
        response = self.client.post('/V2/paraphrase/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('paraphrase', json.loads(response.data.decode()))

    def test_paraphrase_multiple(self):
        data = {"input": "Example text"}
        response = self.client.post('/V2/paraphrase/multiple', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('paraphrases', json.loads(response.data.decode()))