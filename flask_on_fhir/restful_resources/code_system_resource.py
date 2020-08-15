from fhirclient.models.codesystem import *
from .fhir_resource import FHIRResource
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('code', type=str, required=False)
parser.add_argument('system', type=str, required=False)


class CodeSystemResource(FHIRResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def resource_type(cls) -> str:
        return CodeSystem.resource_type


    # @self.fhir.operation('lookup')
    # def lookup(self):
    #     args = parser.parse_args(strict=True)
    #     return 'lookup', 200
