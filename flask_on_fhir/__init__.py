# -*- coding: utf-8 -*-
"""
    flask_on_fhir
    ~~~~
    Flask-on-FHIR is a flask extension helping you to build FHIR API
    :license: MIT, see LICENSE for more details.
"""
from .extension import FHIR

__all__ = ['FHIR']

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

# Set initial level to WARN. Users must manually enable logging for
# flask_cors to see our logging.
rootlogger = logging.getLogger(__name__)
rootlogger.addHandler(NullHandler())

if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)