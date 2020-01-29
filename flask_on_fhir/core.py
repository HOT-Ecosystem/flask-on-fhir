from flask import request, current_app
from collections.abc import Iterable
import logging

LOG = logging.getLogger(__name__)

CONFIG_OPTIONS = []
DEFAULT_OPTIONS = dict()


def get_fhir_options(app, *dicts):
    options = DEFAULT_OPTIONS.copy()
    options.update(get_app_kwarg_dict(app))
    if dicts:
        for d in dicts:
            options.update(d)
    return serialize_options(options)


def get_app_kwarg_dict(app_instance=None):
    app = (app_instance or current_app)
    app_config = getattr(app, 'config', {})
    return {
        k.lower().replace('fhir_', ''): app_config.get(k)
        for k in CONFIG_OPTIONS
        if app_config.get(k) is not None
    }


def ensure_iterable(inst):
    """
    Wraps scalars or string types as a list, or returns the iterable instance.
    """
    if isinstance(inst, str):
        return [inst]
    elif not isinstance(inst, Iterable):
        return [inst]
    else:
        return inst


def serialize_options(opts):
    """
    A helper method to serialize and processes the options dictionary.
    """
    options = (opts or {}).copy()
    for key in opts.keys():
        if key not in DEFAULT_OPTIONS:
            LOG.warning("Unknown option passed to Flask-on-FHIR: %s", key)
    return options


def serialize_option(options_dict, key, upper=False):
    if key in options_dict:
        value = flexible_str(options_dict[key])
        options_dict[key] = value.upper() if upper else value


def flexible_str(obj):
    """
    A more flexible str function which intelligently handles stringifying
    strings, lists and other iterables. The results are lexographically sorted
    to ensure generated responses are consistent when iterables such as Set
    are used.
    """
    if obj is None:
        return None
    elif not isinstance(obj, str) and isinstance(obj, Iterable):
        return ', '.join(str(item) for item in sorted(obj))
    else:
        return str(obj)
