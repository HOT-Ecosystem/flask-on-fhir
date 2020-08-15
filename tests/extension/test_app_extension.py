def test_metadata(client, fhir):
    res = client.get('/metadata')
    assert res.status_code == 200
    assert res.json['resourceType'] == 'CapabilityStatement'


def test_add_rest_operation(client, fhir, code_system):
    class ResourceTest:
        @classmethod
        def resource_type(cls):
            return 'CodeSystem'

        @fhir.read(params={})
        def read(self, resource_id: str):
            return code_system

    assert 'CodeSystem' in fhir.fhir_resources

