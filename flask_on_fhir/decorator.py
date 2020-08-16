import functools
from flask_on_fhir.core import current_fhir


def fhir_read(params={}):
    """
    A decorator that is used in a resource to specify the read operation
    :return: a decorator class
    """

    class Decorator(object):
        """ a decorator for the Read operation"""
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
            if current_fhir:
                current_fhir.add_fhir_resource_read(resource_type, self)

        def __call__(self, *args, **kwargs):
            func = functools.partial(self.fn, self.fn.owner) if hasattr(self.fn, 'owner') else self.fn
            resp = func(*args, **kwargs)
            return resp.as_json(), 200

    return Decorator