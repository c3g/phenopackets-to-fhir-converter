#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='phenopackets-to-fhir',
    version='0.1',
    packages=['converters'],
    url='',
    license='LGPLv3',
    author='Ksenia Zaytseva',
    author_email='',
    description='Library to convert Phenopackets objects to FHIR',
    install_requires=[
        "fhirclient>=3.2,<4.0",
    ]
)
