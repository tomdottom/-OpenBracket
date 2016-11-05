#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='us_census',
    version='0.0.1dev1',
    install_requires=[
        'requests',
        'census'
    ],
    description='Wrapper around processed us census data and external apis',
    author='Tom O. Marks & Chris A. Williams',
    author_email='thomas.o.marks@gmail.com',
    packages=find_packages(),
)
