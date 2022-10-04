from setuptools import setup, find_packages
import pathlib
import os
import sys
import labels


setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires=">=3.7",
    packages=find_packages(where="src"),
    install_requires=[
        'pytest'
    ]
    
)
