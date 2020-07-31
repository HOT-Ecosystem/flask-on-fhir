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

...


