from flask import Flask
from flask_restful import Api
from functools import wraps

from flask_on_fhir.data_engine import CapabilityStatementDataEngine
from flask_on_fhir.restful_resources import CapabilityStatementResource
from flask_on_fhir.core import *

LOG = logging.getLogger(__name__)


class FHIR(Api):

    def __init__(self, app=None, data_engine=None, **kwargs):
        self._options = kwargs
        self.fhir_resources = []
        self.data_engine = data_engine
        super().__init__(app, **kwargs)

    def init_app(self, app: Flask):
        super().init_app(app)
        self.add_resource(CapabilityStatementResource, '/metadata',
                          resource_class_kwargs={'data_engine': CapabilityStatementDataEngine()})
        self.fhir_resources.append(CapabilityStatementResource)

    def add_fhir_resource(self, resource, *urls, **kwargs):
        resource_class_kwargs = kwargs.pop('resource_class_kwargs', {})
        if 'data_engine' not in resource_class_kwargs:
            resource_class_kwargs['data_engine'] = self.data_engine
        kwargs['resource_class_kwargs'] = resource_class_kwargs
        urls.append(f'/{resource.get_resource_type()}')
        urls.append(f'/{resource.get_resource_type()}/<str:resource_id>')
        self.add_resource(resource, *urls, **kwargs)
        self.fhir_resources.append(resource)

    def operation(self, name: str, **kwargs):
        def decorator(func):
            @wraps
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator
