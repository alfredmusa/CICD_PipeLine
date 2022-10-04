from setuptools import setup, find_packages
import pathlib
import os
import sys

setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires=">=3.7",
    install_requires=[
        'cython','pytest','labels','pandas','numpy'
    ],
    packages=find_packages(where="src")
)
