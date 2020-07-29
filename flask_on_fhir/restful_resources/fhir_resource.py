from flask_restful import Resource
from fhirclient.models import resource


class FHIRResource(Resource):
    """
    An extension of the flask-restful Resource. It provides useful methods to process FHIR requests and
    build FHIR responses
    """

    def __init__(self, *args, **kwargs):
        self.data_engine = kwargs.get('data_engine')

    def get_resource_type(self) -> str:
        ...

    def get(self, *args, **kwargs):
        if hasattr(self, 'data_engine'):
            fhir_resource: resource.Resource = self.data_engine.get_fhir_resource(self.get_resource_type(), *args, **kwargs)
            return fhir_resource.as_json(), 200
        else:
            return None




