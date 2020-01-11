from flask import Flask
from typing import Any, Dict, Union
from .core import *
from flask_fhir.resources.capability_statement import CapabilityStatementProvider
LOG = logging.getLogger(__name__)


class FHIR(object):

    def __init__(self, app=None, **kwargs):
        self._options = kwargs
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask, **kwargs):
        app.add_url_rule('/metadata', 'CapabilityStatement',
                         CapabilityStatementProvider.as_view('CapabilityStatement', self), ['GET'])

