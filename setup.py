#!/usr/bin/env python

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='rainbowrunners',
    version='0.0.3.dev0',
    description='Awesome rainbow test runners',
    long_description=read('README.rst'),
    author='Nikita Grishko',
    author_email='grin.minsk@gmail.com',
    packages=find_packages(),
    url='http://gr1n.github.io/rainbowrunners/',
    license='MIT',
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    include_package_data=True,
    zip_safe=False,
)
