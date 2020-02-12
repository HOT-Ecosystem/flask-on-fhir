from flask_restful import Resource


class FHIRResource(Resource):
    """
    An extension of the flask-restful Resource. It provides useful methods to process FHIR requests and
    build FHIR responses
    """

    def get_resource_type(self) -> str:
        ...



