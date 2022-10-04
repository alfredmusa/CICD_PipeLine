from setuptools import setup, find_packages
import pathlib
import os
import sys

setup(
    name='CICD_PipeLine',
    version='7.1.3',
    python_requires=">=3.7",
    setup_requires=[
            "cython",
            'numpy<1.20.0; python_version<"3.7"'
        ],
    install_requires=[
        'cython','pytest','labels','pandas','numpy<1.20.0; python_version<"3.7"
    ],
    packages=find_packages(where="src")
)
