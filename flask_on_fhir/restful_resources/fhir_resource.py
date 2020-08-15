from flask_restful import Resource
from fhirclient.models import resource


class FHIRResource(Resource):
    """
    An extension of the flask-restful Resource. It provides useful methods to process FHIR requests and
    build FHIR responses
    """

    rest_operations = {}
    fhir_operations = {}

    def __init__(self, *args, **kwargs):
        self.data_engine = kwargs.get('data_engine')

    @classmethod
    def resource_type(cls) -> str:
        ...

    def get(self, *args, **kwargs):
        resource_type = self.resource_type()
        if hasattr(self, 'data_engine'):
            fhir_resource: resource.Resource = self.data_engine.get_fhir_resource(resource_type, *args, **kwargs)
            return fhir_resource.as_json(), 200
        else:
            return None

    @classmethod
    def add_rest_operation(cls, name, func):
        cls.rest_operations[name] = func

    @classmethod
    def add_fhir_operation(cls, name, func):
        cls.fhir_operations[name] = func



