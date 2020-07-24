from datetime import datetime
from flask import current_app, url_for
from fhirclient.models.capabilitystatement import *
from fhirclient.models.fhirdate import FHIRDate
from flask_restful import Api, Resource

from .fhir_resource import FHIRResource


class CapabilityStatementResource(FHIRResource):
    method_decorators = []

    def __init__(self, fhir: 'FHIR'):
        self.fhir = fhir

    def get_resource_type(self) -> str:
        return CapabilityStatement.resource_type

    def get(self, *_args, **_kwargs):
        return self._get().as_json(), 200

    def _get(self) -> CapabilityStatement:
        cs: CapabilityStatement = CapabilityStatement()
        cs.fhirVersion = '4.0.0'
        cs.status = 'active'
        cs.acceptUnknown = 'false'
        cs.format = ['json']
        cs.kind = 'json'
        date = FHIRDate()
        date.date = datetime.today()
        cs.date = date
        rest: CapabilityStatementRest = CapabilityStatementRest()
        cs.rest = [rest]
        rest.mode = "server"
        rest.resource = []
        resource: FHIRResource
        for rule in self.fhir.api.app.url_map.iter_rules():
            if rule.endpoint in self.fhir.api.endpoints:
                print(rule)
        # for endpoint in self.api.endpoints:
        #     self.api.app.url_map
        #     res: CapabilityStatementRestResource = CapabilityStatementRestResource()
        #     res.resource_type = resource.get_resource_type()
        #     res.profile = f"http://hl7.org/fhir/StructureDefinition/{res.resource_type}"
        #     rest.resource.append(rest)
        return cs
