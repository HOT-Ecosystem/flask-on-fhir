"""
Flask-on-FHIR
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-on-FHIR',
    version='0.0.1.dev',
    url='http://github.com/jiaola/flask-on-fhir',
    license='BSD',
    author='Dazhi Jiao',
    author_email='djiao@jhu.edu',
    description='A FLASK extension to for building FHIR RESTful API',
    long_description=__doc__,
    packages=['flask_on_fhir', 'flask_on_fhir.resources'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    python_requires='>=3.6',
    # extra_require={
    #     'test': tests_require,
    #     'doc': doc_require,
    #     'dev': dev_require,
    # },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)