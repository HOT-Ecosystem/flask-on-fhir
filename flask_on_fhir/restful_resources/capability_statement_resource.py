from datetime import datetime
from flask import current_app
from fhirclient.models.capabilitystatement import CapabilityStatement, CapabilityStatementRest
from fhirclient.models.fhirdate import FHIRDate

from flask_on_fhir.restful_resources.fhir_resource import FHIRResource


class CapabilityStatementResource(FHIRResource):
    method_decorators = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def resource_type(cls) -> str:
        return CapabilityStatement.resource_type
