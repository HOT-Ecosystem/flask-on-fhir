from fhirclient.models.valueset import ValueSet

from ..base_test import FlaskFHIRTestCase
from flask import Flask, jsonify
from flask_on_fhir import *
from flask_on_fhir.extension import FHIR
from flask_on_fhir.restful_resources import CodeSystemResource


class CodeSystemTestCase(FlaskFHIRTestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.fhir: FHIR = FHIR(self.app)
        self.fhir.add_fhir_resource(CodeSystemResource, '/CodeSystem')

    def test_lookup(self):
        resp = self.get('/lookup')
        print('response', resp.json)




