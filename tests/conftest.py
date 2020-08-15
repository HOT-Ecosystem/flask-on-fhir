import pytest
from fhirclient.models.codesystem import CodeSystem
from flask import Flask
from flask_on_fhir import FHIR, DataEngine
import json


@pytest.fixture
def app():
    app = Flask(__name__)
    return app


@pytest.fixture
def data_engine():
    class TestDataEngine(DataEngine):
        def get_fhir_resource(self, resource: str, *args, **kwargs):
            if resource == 'CodeSystem':
                cs = CodeSystem()
                cs.name = '_Test Code System'
                cs.id = '_1234'
                cs.status = 'active'
                cs.content = 'not-present'
                return cs
    return TestDataEngine()


@pytest.fixture
def fhir(app, data_engine):
    fhir = FHIR(app, data_engine)
    return fhir


@pytest.fixture
def code_system() -> CodeSystem:
    cs: CodeSystem = CodeSystem()
    cs.update_with_json(json.loads("""
    {
          "resourceType": "CodeSystem",
          "id": "summary",
          "url": "http://hl7.org/fhir/CodeSystem/summary",
          "version": "4.0.1",
          "name": "Code system summary example for ACME body sites",
          "status": "draft",
          "experimental": true,
          "publisher": "HL7 International",
          "contact": [
            {
              "name": "FHIR project team",
              "telecom": [
                {
                  "system": "url",
                  "value": "http://hl7.org/fhir"
                }
              ]
            }
          ],
          "description": "This is an example code system summary for the ACME codes for body site.",
          "useContext": [
            {
              "code": {
                "system": "http://example.org/CodeSystem/contexttype",
                "code": "species"
              },
              "valueCodeableConcept": {
                "coding": [
                  {
                    "system": "http://snomed.info/sct",
                    "code": "337915000",
                    "display": "Homo sapiens (organism)"
                  }
                ]
              }
            }
          ],
          "jurisdiction": [
            {
              "coding": [
                {
                  "system": "urn:iso:std:iso:3166",
                  "code": "CA"
                }
              ]
            }
          ],
          "caseSensitive": true,
          "content": "not-present",
          "count": 92
    }
    """))
    return cs
