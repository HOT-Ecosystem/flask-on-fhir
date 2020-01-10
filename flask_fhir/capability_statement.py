from fhirclient.models.capabilitystatement import CapabilityStatement as FHIRCapabilityStatement
from flask.views import MethodView
from flask import Flask, jsonify


class CapabilityStatement(FHIRCapabilityStatement, MethodView):
    def __init__(self, app: Flask):
        self.app = app

    def get(self):
        return jsonify(self.app.__schema__()), 200
