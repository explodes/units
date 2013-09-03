#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

rel = lambda * x: os.path.abspath(os.path.join(os.path.dirname(__file__), *x))

with open(rel('./README.md')) as readme:
    long_description = readme.read()

setup(
    name='units',
    version='0.1.0',
    description="Mathematical units description library.",
    long_description=long_description,
    author='Evan Leis',
    author_email='evan.explodes@gmail.com',
    url='https://github.com/explodes/units',
    install_requires=[
    ],
    setup_requires=[
    ],
    packages=find_packages(exclude=[
    ]),
    include_package_data=True,
    test_suite="units.tests",
    package_data={},
    zip_safe=True,
    entry_points="""
""",
    license="Apache Software License",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
