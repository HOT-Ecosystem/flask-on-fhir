from flask_on_fhir.restful_resources import CodeSystemResource


def test_code_system(client, fhir):
    fhir.add_fhir_resource(CodeSystemResource)
    res = client.get('/CodeSystem')
    assert res.status_code == 200
    assert res.json['resourceType'] == 'CodeSystem'
