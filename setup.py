#!/usr/bin/env python

from distutils.core import setup


try:
    license = open('LICENSE').read()
except:
    license = None


setup(
    name='rainbowrunners',
    version='0.0.1',
    author='Nikita Grishko',
    author_email='grin.minsk@gmail.com',
    packages=['rainbowrunners',],
    url='https://github.com/Gr1N/rainbowrunners',
    license=license,
    description='Awesome rainbow test runners',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
