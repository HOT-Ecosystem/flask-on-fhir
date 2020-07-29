from datetime import datetime

from fhirclient.models.capabilitystatement import CapabilityStatement, CapabilityStatementRest
from fhirclient.models.fhirdate import FHIRDate
from flask import current_app


class DataEngine:
    def __init__(self):
        ...

    def get_fhir_resource(self, resource: str, *args, **kwargs):
        ...


class CapabilityStatementDataEngine(DataEngine):
    def get_fhir_resource(self, resource: str, *args, **kwargs):
        if resource != CapabilityStatement.resource_type:
            ... # throw an error
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
        for rule in current_app.url_map.iter_rules():
            print(rule)
        return cs
        # for endpoint in self.api.endpoints:
        #     self.api.app.url_map
        #     res: CapabilityStatementRestResource = CapabilityStatementRestResource()
        #     res.resource_type = resource.get_resource_type()
        #     res.profile = f"http://hl7.org/fhir/StructureDefinition/{res.resource_type}"
        #     rest.resource.append(rest)

