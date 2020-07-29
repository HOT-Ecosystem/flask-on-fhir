from flask import Flask
from flask_restful import Api
from functools import wraps

from flask_on_fhir.restful_resources import CapabilityStatementResource
from flask_on_fhir.restful_resources import FHIRResource
from flask_on_fhir.core import *

LOG = logging.getLogger(__name__)


class FHIR(Api):

    def __init__(self, app=None, **kwargs):
        self._options = kwargs
        self.fhir_resources = []
        super().__init__(app, **kwargs)

    def init_app(self, app: Flask):
        super().init_app(app)
        self.add_fhir_resource(CapabilityStatementResource, '/metadata')
        self.fhir_resources.append(CapabilityStatementResource)

    def add_fhir_resource(self, resource: FHIRResource, *urls, **kwargs):
        self.add_resource(resource, *urls, **kwargs)

    def operation(self, name: str, **kwargs):
        def decorator(func):
            @wraps
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
