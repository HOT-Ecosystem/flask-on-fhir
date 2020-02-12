from fhirclient.models.valueset import ValueSet

from flask_on_fhir.resources.fhir_resource import FHIRResource
from ..base_test import FlaskFHIRTestCase
from flask import Flask, jsonify
from flask_on_fhir import *
from flask_on_fhir.extension import FHIR


class AppExtension(FlaskFHIRTestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.fhir: FHIR = FHIR(self.app)

        @self.app.route('/test_defaults')
        def wildcard():
            return 'Welcome!'

    def test_metadata(self):
        resp = self.get('/metadata')
        print(resp.json)
        self.assertEqual(resp.json['resourceType'], 'CapabilityStatement')

    def test_add_resource(self):
        class ValueSetResource(FHIRResource):
            def get_resource_type(self):
                return ValueSet.resource_type

            def get(self):
                return "test", 200

        self.fhir.add_fhir_resource(ValueSetResource, '/ValueSet')
        resp = self.get('/metadata')
        print(resp.json)



