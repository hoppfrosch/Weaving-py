# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='weaving',
    version='0.0.1',
    description='Tablet weaving',
    long_description=readme,
    author='hoppfrosch',
    author_email='hoppfrosch@gmx.de',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

