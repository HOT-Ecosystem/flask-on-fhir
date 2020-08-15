from fhirclient.models.bundle import Bundle
from fhirclient.models.identifier import Identifier
from flask_restful import Resource
from fhirclient.models import resource

from flask_on_fhir.core import current_fhir
from functools import wraps


class FHIRResource(Resource):
    """
    An extension of the flask-restful Resource. It provides useful methods to process FHIR requests and
    build FHIR responses
    """

    def __init__(self, *args, **kwargs):
        self.data_engine = kwargs.get('data_engine')

    @classmethod
    def get_resource_type(cls) -> str:
        ...

    def get(self, *args, **kwargs):
        resource_type = self.get_resource_type()
        if hasattr(self, 'data_engine'):
            fhir_resource: resource.Resource = self.data_engine.get_fhir_resource(resource_type, *args, **kwargs)
            return fhir_resource.as_json(), 200
        else:
            return None



