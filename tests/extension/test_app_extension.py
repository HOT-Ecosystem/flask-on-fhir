def test_metadata(client, fhir):
    res = client.get('/metadata')
    assert res.status_code == 200
    assert res.json['resourceType'] == 'CapabilityStatement'


def test_add_rest_operation_in_class(client, fhir, code_system):
    class ResourceTest:
        @classmethod
        def resource_type(cls):
            return 'CodeSystem'

        @fhir.read(params={})
        def read(self, resource_id: str):
            return code_system

    assert 'CodeSystem' in fhir.fhir_resources


def test_add_rest_operation_in_function(client, fhir, code_system):
    @fhir.read(params={})
    def read_op(resource_id: str):
        return code_system

    fhir.add_fhir_resource_read('CodeSystem', read_op)
    assert 'CodeSystem' in fhir.fhir_resources
    assert 'read' in fhir.fhir_resources['CodeSystem'].rest_operations

    res = client.get('/CodeSystem/summary')
    assert res.status_code == 200


