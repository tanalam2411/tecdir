#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='tecdir_project',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='tecdir App',
    # GETTING-STARTED: set author name (your name):
    author='Tanveer Alam',
    # GETTING-STARTED: set author email (your email):
    author_email='tan24alam11@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.11.9'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
