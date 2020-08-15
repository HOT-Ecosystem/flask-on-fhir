# flask-on-fhir

A flask extension to build FHIR RESTful APIs. 

## Installation

```shell script
pip install flask-on-fhir
```

## Quickstart 

```python
from flask import Flask
from flask-on-fhir import FHIR 

app = Flask(__name__)
fhir = FHIR(app)

if __name__ == '__main__':
    app.run()

```

Save this as api.py and run it using your Python interpreter. 
You can also run the app with `app.run(debug=True)` in the last line
to enable Flask debugging mode to provide code 
reloading and better error messages.

```
python api.py
```

Now open up a new prompt to test out your FHIR API using curl

```python
curl http://127.0.0.1:5000/metadata
```

## Implement a FHIR Resource EndPoint

### Use decorator

```python
from fhirclient.models.codesystem import CodeSystem

class CodeSystemResource(object):
    @classmethod
    def resource_type(cls) -> str:
        return CodeSystem.resource_type

    @fhir.read(params={})
    def readme(self, resource_id: str) -> CodeSystem:
        if resource_id == 'summary':
            code_system = CodeSystem()
            code_system.id = 'summary'
            code_system.name = 'Summary Code System'
            return code_system
        else:
            return None

```


