import datetime

from fhirclient.models.capabilitystatement import CapabilityStatement
from fhirclient.models.fhirdate import FHIRDate
from flask import Flask

from flask_on_fhir.resources.resource_provider import ResourceProvider


class CapabilityStatementProvider(ResourceProvider):
    def __init__(self, app: Flask):
        self.app = app

    def get_resource_type(self) -> str:
        return CapabilityStatement.resource_type

    def get(self):
        return self._get().as_json(), 200

    def _get(self) -> CapabilityStatement:
        cs: CapabilityStatement = CapabilityStatement()
        cs.fhirVersion = '4.0.0'
        cs.status = 'active'
        cs.acceptUnknown = 'false'
        cs.format = ['json']
        cs.kind = 'json'
        date = FHIRDate()
        date.date = datetime.datetime.today()
        cs.date = date
        return cs
