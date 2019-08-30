# -*- coding: utf-8 -*-
# Author: Forrest Smith
from setuptools import setup


setup(name='resistor',
      version='0.1',
      description='A simple module for representing a resistor.',
      url='https://github.com/ephsmith/resistor',
      author='Forrest Smith',
      author_email='fasmith0229@gmail.com',
      license='MIT',
      packages=['resistor'],
      install_requires=[
          'si_prefix',
          'Pillow',
          ],
      zip_safe=False)
