import pytest
from flask_on_fhir.core import current_fhir
from fhirclient.models.identifier import Identifier
from fhirclient.models.resource import Resource
from fhirclient.models.codesystem import CodeSystem
import json

from flask_on_fhir.restful_resources import FHIRResource


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


def test_fhir_read(fhir, client, code_system):
    # @fhir_resource(name="CodeSystem")
    class ReadTest(FHIRResource):
        local_code_system = code_system
        @classmethod
        def resource_type(cls) -> str:
            return CodeSystem.resource_type

        @fhir.read(params={})
        def readme(self, resource_id: str) -> CodeSystem:
            if resource_id == 'summary':
                return self.local_code_system
            else:
                return None

    cs, port = ReadTest().readme('summary')
    assert cs['resourceType'] == 'CodeSystem'

    res = client.get('/CodeSystem/summary')
    assert res.status_code == 200
    assert res.json['resourceType'] == 'CodeSystem'
    assert res.json['id'] == 'summary'





