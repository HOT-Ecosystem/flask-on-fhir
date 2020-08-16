import pytest
from flask_on_fhir.core import current_fhir
from fhirclient.models.identifier import Identifier
from fhirclient.models.resource import Resource
from fhirclient.models.codesystem import CodeSystem
from flask_on_fhir.decorator import fhir_read
import json

from flask_on_fhir.restful_resources import FHIRResource


def test_fhir_read(fhir, client, code_system):
    # @fhir_resource(name="CodeSystem")
    class ReadTest(object):
        local_code_system = code_system
        @classmethod
        def resource_type(cls) -> str:
            return CodeSystem.resource_type

        @fhir_read(params={})
        def readme(self, resource_id: str) -> CodeSystem:
            if resource_id == 'summary':
                return self.local_code_system
            else:
                return None

    # test with decorator
    cs, port = ReadTest().readme('summary')
    assert cs['resourceType'] == 'CodeSystem'

    # test the wrapped function without decorator
    rt = ReadTest()
    cs = rt.readme.__wrapped__(rt, 'summary')
    assert cs.resource_type == 'CodeSystem'

    res = client.get('/CodeSystem/summary')
    assert res.status_code == 200
    assert res.json['resourceType'] == 'CodeSystem'
    assert res.json['id'] == 'summary'





