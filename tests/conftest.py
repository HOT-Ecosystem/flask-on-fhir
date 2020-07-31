import pytest
from fhirclient.models.codesystem import CodeSystem
from flask import Flask
from flask_on_fhir import FHIR, DataEngine


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
