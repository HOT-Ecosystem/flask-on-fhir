from fhirclient.models.bundle import Bundle
from flask import Flask, _app_ctx_stack, current_app
from flask_restful import Api
import functools
from typing import Callable

from flask_on_fhir.data_engine import CapabilityStatementDataEngine
from flask_on_fhir.restful_resources import CapabilityStatementResource
import logging

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
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'fhir'):
                ctx.fhir = self

    def add_fhir_resource(self, resource, *urls, **kwargs):
        resource_class_kwargs = kwargs.pop('resource_class_kwargs', {})
        if 'data_engine' not in resource_class_kwargs:
            resource_class_kwargs['data_engine'] = self.data_engine
        kwargs['resource_class_kwargs'] = resource_class_kwargs
        urls = list(urls)
        urls.append(f'/{resource.get_resource_type()}')
        urls.append(f'/{resource.get_resource_type()}/<resource_id>')
        self.add_resource(resource, *urls, **kwargs)
        self.fhir_resources.append(resource)

    def add_fhir_resource_read(self, resource_type: str, func: Callable):
        # just add the url for now. TODO: Manage resources
        url = f'/{resource_type}/<resource_id>'
        current_app.add_url_rule(url, resource_type, func)

    def read(self, params={}):
        """
        A decorator that is used in a resource to specify the read operation
        :return: a decorator class
        """
        fhir_app = self

        class Decorator(object):
            """ a decorator for the Read operation"""
            local_fhir_app = fhir_app
            local_params = params

            def __init__(self, fn):
                functools.update_wrapper(self, fn)
                self.fn = fn

            def __set_name__(self, owner, name):
                if owner:
                    self.fn.owner = owner
                resource_type_op = getattr(owner, 'resource_type', None)
                if callable(resource_type_op):
                    resource_type = owner.resource_type()
                else:
                    ...  # throw an exception

                self.local_fhir_app.add_fhir_resource_read(resource_type, self)

            def __call__(self, *args, **kwargs):
                func = functools.partial(self.fn, self.fn.owner) if hasattr(self.fn, 'owner') else self.fn
                resp = func(*args, **kwargs)
                if isinstance(resp, Bundle):
                    # do something about bundle?
                    ...
                return resp.as_json(), 200

        return Decorator


