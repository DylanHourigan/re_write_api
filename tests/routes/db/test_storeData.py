from flask_testing import TestCase
from flask import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))


from ....app import create_app

class TestStoreData(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_store_data(self):
        data = {
            "referenceText": "Sample reference",
            "generatedText": "Sample generated text"
        }
        response = self.client.post('/storeData/', data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], 'Data inserted successfully')
