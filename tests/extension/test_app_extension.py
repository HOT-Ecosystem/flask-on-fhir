from ..base_test import FlaskFHIRTestCase
from flask import Flask, jsonify
from flask_on_fhir import *


class AppExtension(FlaskFHIRTestCase):
    def setUp(self):
        self.app = Flask(__name__)
        FHIR(self.app)

        @self.app.route('/test_defaults')
        def wildcard():
            return 'Welcome!'

    def test_metadata(self):
        for resp in self.iter_responses('/metadata'):
            self.assertEqual(resp.json['resourceType'], 'CapabilityStatement')
