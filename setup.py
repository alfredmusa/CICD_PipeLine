from setuptools import setup, find_packages
import pathlib
import os
import sys


setup(
    name='CICD_PipeLine',
    version='7.1.3',
    setup_requires=SETUP_REQUIRES,
    python_requires='>=3.8',
    install_requires=[
        'cython','pytest','labels','pandas','numpy'
    ],
    packages=find_packages(where="src")
)
