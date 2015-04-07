#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='django_view_dispatch',
      version='0.1',
      description='Django utility to dispatch views based on request method',
      author='Laurent Peuch',
      #long_description='',
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/django_view_dispatch',
      install_requires=['weirdict'],
      py_modules=['django_view_dispatch'],
      license= 'BSD',
      keywords='django',
     )
