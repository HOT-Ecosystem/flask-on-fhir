from flask import request, Flask
from typing import Any, Dict, Optional, Union
from .core import *
from .capability_statement import CapabilityStatement
LOG = logging.getLogger(__name__)


class FHIR(object):

    def __init__(self, app=None, **kwargs):
        self._options = kwargs
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask, **kwargs):
        app.add_url_rule('/metadata', 'CapabilityStatement',
                         CapabilityStatement.as_view('CapabilityStatement', self), ['GET'])
        # options = get_fhir_options(app, self._options, kwargs)
        #
        # resources = parse_resources(options.get('resources'))
        # cors_after_request = make_after_request_function(resources)

    def __schema__(self) -> Dict[str, Union[str, Dict[str, Any]]]:
        return {"resourceType": "CapabilityStatement"}

