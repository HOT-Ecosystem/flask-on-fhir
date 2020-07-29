from flask_restful import Resource
from fhirclient.models import resource


class FHIRResource(Resource):
    """
    An extension of the flask-restful Resource. It provides useful methods to process FHIR requests and
    build FHIR responses
    """

    def get_resource_type(self) -> str:
        ...

    def get(self, *_args, **_kwargs):
        return self.build_resource().as_json(), 200

    def build_resource(self) -> resource.Resource:
        ...



