from flask import current_app, _app_ctx_stack

class FHIR(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('FHIR_VERSION', ':4.0.0:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        pass

    def teardown(self):
        pass

