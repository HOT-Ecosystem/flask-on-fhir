from flask import Flask
import unittest
from flask_on_fhir import *


class FlaskFHIRTestCase(unittest.TestCase):
    def get(self, *args, **kwargs):
        return self._request('get', *args, **kwargs)

    def _request(self, verb, *args, **kwargs):
        headers = kwargs.pop('headers', {})
        with self.app.test_client() as c:
            return getattr(c, verb)(*args, headers=headers, **kwargs)

    def iter_responses(self, path, verbs=['get'], **kwargs):
        for verb in verbs:
            yield self._request(verb.lower(), path, **kwargs)
