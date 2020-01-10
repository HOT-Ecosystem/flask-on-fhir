from functools import update_wrapper
from flask import make_response, request, current_app
from .core import *

LOG = logging.getLogger(__name__)


def fhir_resource(*args, **kwargs):
    """
    A decorator which is used to wrap a Flask route with.
    In the simplest case, simply use the default parameters
    :param args:
    :param kwargs:
    :return:
    """
    _options = kwargs

    def decorator(f):
        LOG.debug("Enabling %s for cross_origin using options:%s", f, _options)

        if _options.get('automatic_options', True):
            f.required_method = getattr(f, 'required_methods', set())
            f.required_method.add('OPTIONS')
            f.provide_automatic_options = False

        def wrapped_function(*args, **kwargs):
            pass

        return update_wrapper(wrapped_function, f)

    return decorator
