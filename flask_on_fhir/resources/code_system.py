from fhirclient.models.codesystem import *
from .fhir_resource import FHIRResource
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('code', type=str, required=False)
parser.add_argument('system', type=str, required=False)


class CodeSystemResource(FHIRResource):
    def __init__(self, fhir: 'FHIR'):
        self.fhir = fhir

    # @self.fhir.operation('lookup')
    # def lookup(self):
    #     args = parser.parse_args(strict=True)
    #     return 'lookup', 200
