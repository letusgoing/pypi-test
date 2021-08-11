#!/usr/bin/env python


from __future__ import print_function
from setuptools import setup, find_packages
import sys


setup(
    name="pypi-test-harvey",
    version='0.1.2',
    author="harvey",
    author_email='',
    describtion='hello',
    long_description=open("README.rst").read(),
    license='GPL',
    url='https://github.com/letusgoing/pypi-test.git',
    packages=['pypiTest'],
    install_requires=[],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

)
