from flask_restful import Api
from functools import wraps

from .resources.capability_statement import CapabilityStatementResource
from .resources.fhir_resource import FHIRResource
from .core import *

LOG = logging.getLogger(__name__)


class FHIR(object):

    def __init__(self, app=None, **kwargs):
        self._options = kwargs
        self.resources = []
        if app is not None:
            self.api = Api(app)
            self.init_app(self.api)

    def init_app(self, api: Api, **kwargs):
        # app.add_url_rule('/metadata', 'CapabilityStatement',
        #                  CapabilityStatementProvider.as_view('CapabilityStatement', self), ['GET'])
        self.add_fhir_resource(CapabilityStatementResource, '/metadata', resource_class_kwargs={'fhir': self})

    def add_fhir_resource(self, resource: FHIRResource, *urls, **kwargs):
        self.api.add_resource(resource, *urls, **kwargs)
        self.resources.append(resource)

    def operation(self, name: str, **kwargs):
        def decorator(func):
            @wraps
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


