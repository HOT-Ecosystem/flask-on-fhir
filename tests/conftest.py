import pytest
from flask import Flask
from flask_on_fhir import FHIR


@pytest.fixture
def app():
    app = Flask(__name__)
    return app


@pytest.fixture
def fhir(app):
    fhir = FHIR(app)
    return fhir
