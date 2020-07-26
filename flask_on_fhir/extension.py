from flask import Flask
from flask_restful import Api
from functools import wraps

from .resources.capability_statement import CapabilityStatementResource
from .resources.fhir_resource import FHIRResource
from .core import *

LOG = logging.getLogger(__name__)


class FHIR(Api):

    def __init__(self, app=None, **kwargs):
        super().__init__(app)
        self._options = kwargs

    def init_app(self, app: Flask):
        super().init_app(app)
        self.add_fhir_resource(CapabilityStatementResource, '/metadata')

    def add_fhir_resource(self, resource: FHIRResource, *urls, **kwargs):
        self.add_resource(resource, *urls, **kwargs)

    def operation(self, name: str, **kwargs):
        def decorator(func):
            @wraps
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
