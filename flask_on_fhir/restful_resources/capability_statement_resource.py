from datetime import datetime
from flask import current_app
from fhirclient.models.capabilitystatement import CapabilityStatement, CapabilityStatementRest
from fhirclient.models.fhirdate import FHIRDate
from typing import Type

from flask_on_fhir.decorator import fhir_read
from flask_on_fhir.restful_resources.fhir_resource import FHIRResource
from flask_on_fhir.core import current_fhir


class CapabilityStatementResource(FHIRResource):
    method_decorators = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def resource_type(cls) -> str:
        return CapabilityStatement.resource_type

    @fhir_read(params={})
    def read(self, resource_id: str) -> Type:
        return CapabilityStatement()
